#!/usr/bin/env python3
"""
nexus4_leak_blindness.py
========================

Project Nexus 4 -- Objective C experiment.

QUESTION
--------
The Nexus slow-drift claim is that the architecture's stability barriers cannot
detect arbitrarily slow change. THDE's discrete form is a LEAKY accumulator:

    q_{k+1} = lambda * q_k + severity_k        with theta_on > theta_off

The claim under test is that a leaky accumulator has a sensitivity floor that
does NOT improve with observation length, while a non-leaking accumulator's
sensitivity keeps improving as ~1/sqrt(N).

This script measures that, plus four other things the argument turns on:
reversal behaviour (Green Sky is blue -> green -> blue, not blue -> green),
reference migration policy, world-vs-instrument identifiability, and whether
CUSUM -- the fix five reviewers prescribed -- actually helps.

Every detector is auto-calibrated on the null condition to the SAME target
false-alarm rate before being compared. No detector is strawmanned.

DEPENDENCIES: python3, numpy. Nothing else. No network. No plotting.
DETERMINISM:  fixed seeds; identical output on any machine with the same numpy.

USAGE
-----
    python3 nexus4_leak_blindness.py
    python3 nexus4_leak_blindness.py --seeds 40 --years 800 --json out.json

Report goes to stdout as markdown. Machine-readable results go to --json.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import sys
from dataclasses import dataclass, field, asdict

import numpy as np

SCRIPT_VERSION = "1.1.0"

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

TICKS_PER_YEAR = 12          # one tick = one month
BLUE_YEARS = 500             # initial blue epoch
TRANS_YEARS = 150            # duration of each transition (the slow part)
GREEN_YEARS = 150            # duration of the green plateau
TAIL_YEARS = 100             # blue again, after the return
DEFAULT_YEARS = BLUE_YEARS + TRANS_YEARS + GREEN_YEARS + TRANS_YEARS + TAIL_YEARS

SIGMA = 1.0                  # observation noise (arbitrary units)
AMPLITUDE = 6.0              # total displacement of the Green Sky excursion

TARGET_FALSE_ALARM = 0.05    # calibrate every detector to 5% FA over a full run
CALIB_SEEDS = 200            # null runs used for calibration


# ---------------------------------------------------------------------------
# Signal generation
# ---------------------------------------------------------------------------

@dataclass
class Signal:
    name: str
    x: np.ndarray                     # channel 1 observations
    x2: np.ndarray | None = None      # channel 2 (independent instrument)
    world: np.ndarray | None = None   # ground truth world state
    bias: np.ndarray | None = None    # ground truth instrument bias
    events: dict = field(default_factory=dict)   # label -> tick index
    note: str = ""


def _noise(rng: np.random.Generator, n: int) -> np.ndarray:
    return rng.normal(0.0, SIGMA, size=n)


def make_signal(kind: str, seed: int, n: int) -> Signal:
    """Build one observation stream.

    CRITICAL: 'creep' (world drifts) and 'instrument' (sensor drifts) are
    constructed to produce BIT-IDENTICAL channel-1 observations. That identity
    is asserted in run_self_tests(). It is the point of condition E.
    """
    rng = np.random.default_rng(seed)
    eps = _noise(rng, n)
    zeros = np.zeros(n)
    t = np.arange(n)

    onset = BLUE_YEARS * TICKS_PER_YEAR                       # transition begins
    up_end = onset + TRANS_YEARS * TICKS_PER_YEAR             # green reached
    plateau_end = up_end + GREEN_YEARS * TICKS_PER_YEAR       # return begins
    down_end = plateau_end + TRANS_YEARS * TICKS_PER_YEAR     # blue again
    rate = AMPLITUDE / (TRANS_YEARS * TICKS_PER_YEAR)

    # monotone ramp: flat, rise over the transition window, then hold
    ramp = np.clip((t - onset) * rate, 0.0, AMPLITUDE)

    if kind == "null":
        return Signal("null", eps, x2=_noise(np.random.default_rng(seed + 10**6), n),
                      world=zeros, bias=zeros,
                      note="stationary noise, no drift, no shock")

    if kind == "creep":
        return Signal("creep", ramp + eps,
                      x2=ramp + _noise(np.random.default_rng(seed + 10**6), n),
                      world=ramp, bias=zeros, events={"onset": onset},
                      note="world drifts; both instruments see it")

    if kind == "instrument":
        # identical observations to 'creep' on channel 1, but the cause is the
        # sensor, and channel 2 is unaffected.
        return Signal("instrument", ramp + eps,
                      x2=_noise(np.random.default_rng(seed + 10**6), n),
                      world=zeros, bias=ramp, events={"onset": onset},
                      note="instrument 1 drifts; world is stable")

    if kind == "greensky":
        # blue -> (slow transition) -> green plateau -> (slow return) -> blue
        back = np.clip((t - plateau_end) * rate, 0.0, AMPLITUDE)
        w = ramp - back
        return Signal("greensky", w + eps,
                      x2=w + _noise(np.random.default_rng(seed + 10**6), n),
                      world=w, bias=zeros,
                      events={"onset": onset, "plateau_start": up_end,
                              "reversal": plateau_end, "settled": down_end},
                      note="blue -> green -> blue; the original thought experiment")

    if kind == "shock":
        w = np.where(np.arange(n) >= onset, AMPLITUDE, 0.0)
        return Signal("shock", w + eps,
                      x2=w + _noise(np.random.default_rng(seed + 10**6), n),
                      world=w, bias=zeros, events={"onset": onset},
                      note="step change; the case existing defenses handle")

    if kind == "confound":
        # world drifts up at half rate, instrument drifts down at half rate:
        # channel 1 sees almost nothing while both are moving.
        half = ramp / 2.0
        return Signal("confound", (half + (-half)) + eps,
                      x2=half + _noise(np.random.default_rng(seed + 10**6), n),
                      world=half, bias=-half, events={"onset": onset},
                      note="world and instrument drift in opposite directions")

    raise ValueError(f"unknown signal kind: {kind}")


SIGNAL_KINDS = ["null", "creep", "instrument", "greensky", "shock", "confound"]


# ---------------------------------------------------------------------------
# Detectors
#
# Every detector returns a boolean alarm array of the same length as x.
# Every detector takes a single scalar threshold `h` so calibration is uniform.
# ---------------------------------------------------------------------------

def d_leaky(x: np.ndarray, h: float, lam: float = 0.99, mu: float = 0.0) -> np.ndarray:
    """THDE form: q_{k+1} = lam*q_k + severity_k, severity = |x - mu| >= 0."""
    q = 0.0
    out = np.empty(len(x), dtype=bool)
    for k in range(len(x)):
        q = lam * q + abs(x[k] - mu)
        out[k] = q >= h
    return out


def d_raw_fixed(x: np.ndarray, h: float, mu: float = 0.0) -> np.ndarray:
    """Non-leaking accumulator with a FIXED threshold. Expected to be useless:
    a non-negative severity sum crosses any fixed h given enough time."""
    q = 0.0
    out = np.empty(len(x), dtype=bool)
    for k in range(len(x)):
        q += abs(x[k] - mu)
        out[k] = q >= h
    return out


def d_raw_sqrt(x: np.ndarray, h: float, mu: float = 0.0) -> np.ndarray:
    """Non-leaking accumulator of CENTERED innovations with a sqrt(k)-scaled
    threshold. Under the null, S_k is a random walk with sd ~ sigma*sqrt(k), so
    S_k / sqrt(k) is stationary. This is the candidate repair."""
    s = 0.0
    out = np.empty(len(x), dtype=bool)
    for k in range(len(x)):
        s += (x[k] - mu)
        out[k] = abs(s) >= h * math.sqrt(k + 1)
    return out


def d_cusum1(x: np.ndarray, h: float, nu: float = 0.5, mu: float = 0.0) -> np.ndarray:
    """One-sided CUSUM: C_k = max(0, C_{k-1} + (x_k - mu) - nu)."""
    c = 0.0
    out = np.empty(len(x), dtype=bool)
    for k in range(len(x)):
        c = max(0.0, c + (x[k] - mu) - nu)
        out[k] = c >= h
    return out


def d_cusum2(x: np.ndarray, h: float, nu: float = 0.5, mu: float = 0.0) -> np.ndarray:
    """Two-sided CUSUM."""
    cp = 0.0
    cm = 0.0
    out = np.empty(len(x), dtype=bool)
    for k in range(len(x)):
        r = x[k] - mu
        cp = max(0.0, cp + r - nu)
        cm = min(0.0, cm + r + nu)
        out[k] = (cp >= h) or (cm <= -h)
    return out


def d_refbank(x: np.ndarray, h: float, tau: float = 240.0,
              refs: tuple = (0.0,)) -> np.ndarray:
    """Multi-reference epoch bank.

    Maintains an EWMA of the observation and compares it to every retained epoch
    reference. Alarms when the EWMA is further than h from EVERY retained
    reference -- i.e. 'the current regime matches no epoch I know about'.

    Reversal is handled natively: returning to a previously retained reference
    clears the alarm without needing a signed statistic.
    """
    alpha = 1.0 / tau
    m = x[0]
    ref_arr = np.asarray(refs, dtype=float)
    out = np.empty(len(x), dtype=bool)
    for k in range(len(x)):
        m += alpha * (x[k] - m)
        out[k] = np.min(np.abs(m - ref_arr)) >= h
    return out


def d_crosschannel(x: np.ndarray, x2: np.ndarray, h: float,
                   tau: float = 240.0) -> np.ndarray:
    """Differential detector across two independent instruments.

    Monitors the EWMA of (x - x2). A change common to both channels cancels; a
    change in only one channel does not. This is the minimum mechanism that can
    separate world drift from instrument drift.
    """
    alpha = 1.0 / tau
    m = 0.0
    out = np.empty(len(x), dtype=bool)
    for k in range(len(x)):
        m += alpha * ((x[k] - x2[k]) - m)
        out[k] = abs(m) >= h
    return out


# ---------------------------------------------------------------------------
# Detector registry
# ---------------------------------------------------------------------------

@dataclass
class Detector:
    key: str
    label: str
    fn: object
    kwargs: dict = field(default_factory=dict)
    two_channel: bool = False
    h: float = float("nan")     # filled by calibration


def build_detectors() -> list[Detector]:
    dets: list[Detector] = []
    for lam in (0.90, 0.99, 0.999):
        tau = 1.0 / (1.0 - lam)
        dets.append(Detector(
            f"leaky_l{lam}", f"Leaky accumulator (THDE), lambda={lam} (tau={tau:.0f})",
            d_leaky, {"lam": lam}))
    dets.append(Detector("raw_fixed", "Raw accumulator, fixed threshold", d_raw_fixed))
    dets.append(Detector("raw_sqrt", "Raw accumulator, sqrt(k) threshold", d_raw_sqrt))
    for nu in (0.5, 0.1, 0.02):
        dets.append(Detector(f"cusum1_v{nu}", f"One-sided CUSUM, nu={nu}",
                             d_cusum1, {"nu": nu}))
    dets.append(Detector("cusum2_v0.1", "Two-sided CUSUM, nu=0.1", d_cusum2, {"nu": 0.1}))
    dets.append(Detector("refbank", "Multi-reference epoch bank", d_refbank))
    dets.append(Detector("crosschannel", "Cross-channel differential (2 instruments)",
                         d_crosschannel, two_channel=True))
    return dets


# ---------------------------------------------------------------------------
# Calibration: every detector gets the SAME null false-alarm rate
# ---------------------------------------------------------------------------

def calibrate(det: Detector, n: int, seeds: int, target_fa: float) -> float:
    """Find the smallest h giving <= target_fa false alarms on the null.

    Uses the per-run maximum of the detector statistic. Rather than re-deriving
    each statistic analytically, we bisect on h using the alarm outcome, which
    works for every detector uniformly because all are monotone in h.
    """
    lo, hi = 1e-6, 1.0
    # expand upper bound until the null stops alarming
    for _ in range(80):
        fa = _null_fa(det, n, seeds, hi)
        if fa <= target_fa:
            break
        hi *= 2.0
    else:
        return hi
    for _ in range(45):
        mid = 0.5 * (lo + hi)
        if _null_fa(det, n, seeds, mid) <= target_fa:
            hi = mid
        else:
            lo = mid
    return hi


def _null_fa(det: Detector, n: int, seeds: int, h: float) -> float:
    hits = 0
    for s in range(seeds):
        sig = make_signal("null", 90000 + s, n)
        if det.two_channel:
            a = det.fn(sig.x, sig.x2, h, **det.kwargs)
        else:
            a = det.fn(sig.x, h, **det.kwargs)
        if a.any():
            hits += 1
    return hits / seeds


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def first_alarm(a: np.ndarray) -> int | None:
    idx = np.flatnonzero(a)
    return int(idx[0]) if idx.size else None


def evaluate(det: Detector, kind: str, n: int, seeds: int) -> dict:
    fired, delays, latched, cleared, realarm = 0, [], [], 0, 0
    for s in range(seeds):
        sig = make_signal(kind, 1000 + s, n)
        if det.two_channel:
            a = det.fn(sig.x, sig.x2, det.h, **det.kwargs)
        else:
            a = det.fn(sig.x, det.h, **det.kwargs)
        fa = first_alarm(a)
        if fa is not None:
            fired += 1
        onset = sig.events.get("onset")
        if onset is not None and fa is not None and fa >= onset:
            delays.append((fa - onset) / TICKS_PER_YEAR)
        ps = sig.events.get("plateau_start")
        rev = sig.events.get("reversal")
        settled = sig.events.get("settled")
        if ps is not None and rev is not None and settled is not None:
            plateau = a[ps:rev]          # sky is genuinely, stably green here
            latched.append(float(plateau.mean()) if plateau.size else 0.0)
            tail = a[settled:]           # sky is blue again here
            if tail.size:
                if tail.any():
                    realarm += 1
                else:
                    cleared += 1
    out = {
        "fire_rate": fired / seeds,
        "median_delay_years": float(np.median(delays)) if delays else None,
        "detected_before_end": len(delays) / seeds,
    }
    if latched:
        out["latched_fraction_of_green"] = float(np.mean(latched))
        out["cleared_after_return"] = cleared / seeds
        out["still_alarming_after_return"] = realarm / seeds
    return out


def horizon_robustness(det: Detector, n: int, seeds: int,
                       factors=(1, 4, 16)) -> dict:
    """Calibrate at horizon n, then measure the null false-alarm rate at longer
    horizons.

    This is the 10,000-year question in one measurement. A detector whose
    calibration is horizon-dependent is useless to an individual whose operating
    lifetime is not known in advance: it will be correctly tuned on the day it
    is commissioned and screaming a century later, having observed nothing.
    """
    out = {}
    for f in factors:
        hits = 0
        for s in range(seeds):
            sig = make_signal("null", 77000 + s, n * f)
            if det.two_channel:
                a = det.fn(sig.x, sig.x2, det.h, **det.kwargs)
            else:
                a = det.fn(sig.x, det.h, **det.kwargs)
            if a.any():
                hits += 1
        out[f"x{f}"] = hits / seeds
    return out


def min_detectable_rate(det: Detector, n: int, seeds: int) -> float | None:
    """Smallest constant drift rate (units of sigma per YEAR) the detector
    catches within the run, at its calibrated false-alarm rate.

    This is the headline metric. The leak-blindness claim predicts that this
    value is much larger for leaky detectors than for non-leaking ones.
    """
    def catches(rate_per_year: float) -> bool:
        hits = 0
        rate = rate_per_year / TICKS_PER_YEAR
        for s in range(seeds):
            rng = np.random.default_rng(5000 + s)
            x = np.arange(n) * rate + rng.normal(0.0, SIGMA, n)
            if det.two_channel:
                x2 = np.arange(n) * rate + np.random.default_rng(6000 + s).normal(0, SIGMA, n)
                a = det.fn(x, x2, det.h, **det.kwargs)
            else:
                a = det.fn(x, det.h, **det.kwargs)
            if a.any():
                hits += 1
        return hits / seeds >= 0.5

    lo, hi = 1e-6, 1.0
    if not catches(hi):
        return None
    for _ in range(22):
        mid = math.sqrt(lo * hi)
        if catches(mid):
            hi = mid
        else:
            lo = mid
    return hi


# ---------------------------------------------------------------------------
# Pre-registered predictions
#
# These are written BEFORE the run. Each is checked mechanically. A FAIL is a
# real result, not a bug. P1, P3 and P7 are analytically derivable and are
# included as executable confirmations, not discoveries -- they are marked so.
# ---------------------------------------------------------------------------

PREDICTIONS = [
    ("P1", "analytic",
     "Leaky detectors have a minimum-detectable-rate at least 3x worse than "
     "raw_sqrt, and it does NOT improve as lambda->1 fast enough to close the gap."),
    ("P2", "empirical",
     "Every detector fires on the SHOCK condition. Fast shocks are not the problem."),
    ("P3", "analytic",
     "raw_fixed cannot be calibrated: it either alarms on the null or never "
     "alarms at all. It measures elapsed time, not departure."),
    ("P4", "empirical",
     "CUSUM with nu=0.5 is blind to the Green Sky drift rate (fire_rate < 0.5 "
     "on 'creep'). CUSUM does not automatically fix slow drift; nu is a floor."),
    ("P5", "empirical",
     "raw_sqrt has the lowest minimum-detectable-rate of all single-channel "
     "detectors tested."),
    ("P6", "empirical",
     "With a FIXED reference, at least one detector stays latched for >50% of "
     "the green plateau -- i.e. it spends 150 years reporting that a genuinely "
     "green sky is anomalous."),
    ("P7", "analytic",
     "Conditions 'creep' and 'instrument' produce identical channel-1 streams, "
     "so every single-channel detector gives identical results on both. "
     "Integral tracking alone cannot solve the instrument problem."),
    ("P8", "empirical",
     "The cross-channel detector fires on 'instrument' and NOT on 'creep', "
     "separating world change from instrument change."),
]


def check_predictions(results: dict, mdr: dict) -> list[dict]:
    out = []

    def rec(pid, verdict, evidence):
        out.append({"id": pid, "verdict": verdict, "evidence": evidence})

    leaky_keys = [k for k in mdr if k.startswith("leaky_")]
    best_leaky = min((mdr[k] for k in leaky_keys if mdr[k] is not None), default=None)
    sq = mdr.get("raw_sqrt")
    if best_leaky is None or sq is None:
        rec("P1", "INDETERMINATE", f"best_leaky={best_leaky} raw_sqrt={sq}")
    else:
        rec("P1", "PASS" if best_leaky >= 3 * sq else "FAIL",
            f"best leaky MDR={best_leaky:.5f}, raw_sqrt MDR={sq:.5f}, "
            f"ratio={best_leaky / sq:.2f}x")

    shock = {k: results[k]["shock"]["fire_rate"] for k in results}
    rec("P2", "PASS" if all(v >= 0.95 for k, v in shock.items()
                            if k != "crosschannel") else "FAIL",
        f"fire rates on shock: {shock}")

    rf = results.get("raw_fixed", {})
    rec("P3", "PASS" if rf.get("null", {}).get("fire_rate", 0) > 0.5
        or rf.get("creep", {}).get("fire_rate", 1) < 0.5 else "FAIL",
        f"raw_fixed null fire={rf.get('null', {}).get('fire_rate')}, "
        f"creep fire={rf.get('creep', {}).get('fire_rate')}")

    c05 = results.get("cusum1_v0.5", {}).get("creep", {}).get("fire_rate")
    rec("P4", "PASS" if c05 is not None and c05 < 0.5 else "FAIL",
        f"cusum1 nu=0.5 fire_rate on creep = {c05}")

    single = {k: v for k, v in mdr.items() if k != "crosschannel" and v is not None}
    if sq is not None and single:
        best = min(single, key=lambda k: single[k])
        rec("P5", "PASS" if best == "raw_sqrt" else "FAIL",
            f"lowest MDR is '{best}' at {single[best]:.5f}; raw_sqrt={sq:.5f}")
    else:
        rec("P5", "INDETERMINATE", "insufficient MDR data")

    latch = {k: v["greensky"].get("latched_fraction_of_green")
             for k, v in results.items() if "latched_fraction_of_green" in v["greensky"]}
    worst = max((v for v in latch.values() if v is not None), default=None)
    rec("P6", "PASS" if worst is not None and worst > 0.5 else "FAIL",
        f"max latched fraction of green plateau = {worst}; per-detector: {latch}")

    same = all(
        results[k]["creep"] == results[k]["instrument"]
        for k in results if k != "crosschannel")
    rec("P7", "PASS" if same else "FAIL",
        "single-channel results identical on creep vs instrument"
        if same else "MISMATCH -- generator identity broken, investigate")

    cc = results.get("crosschannel", {})
    ok = (cc.get("instrument", {}).get("fire_rate", 0) >= 0.9
          and cc.get("creep", {}).get("fire_rate", 1) <= 0.1)
    rec("P8", "PASS" if ok else "FAIL",
        f"crosschannel fire rates: instrument="
        f"{cc.get('instrument', {}).get('fire_rate')}, "
        f"creep={cc.get('creep', {}).get('fire_rate')}")
    return out


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------

def run_self_tests(n: int) -> list[str]:
    msgs = []
    a = make_signal("creep", 7, n)
    b = make_signal("instrument", 7, n)
    assert np.array_equal(a.x, b.x), \
        "generator invariant broken: creep and instrument must be identical on ch1"
    msgs.append("OK  creep and instrument channel-1 streams are bit-identical")
    assert not np.array_equal(a.x2, b.x2), "channel 2 must differ"
    msgs.append("OK  channel-2 streams differ (world vs instrument cause)")
    g = make_signal("greensky", 7, n)
    assert abs(g.world[-1]) < 1e-9, "green sky must return to baseline"
    msgs.append("OK  green sky returns exactly to the original baseline")
    assert abs(g.world.max() - AMPLITUDE) < 1e-9, "plateau must reach amplitude"
    msgs.append("OK  green plateau reaches full amplitude")
    ps, rev = g.events["plateau_start"], g.events["reversal"]
    assert np.allclose(g.world[ps:rev], AMPLITUDE), "plateau must be flat"
    msgs.append(f"OK  green plateau is flat for {GREEN_YEARS} years "
                f"(ticks {ps}..{rev})")
    return msgs


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seeds", type=int, default=20,
                    help="evaluation seeds per condition (default 20)")
    ap.add_argument("--calib-seeds", type=int, default=CALIB_SEEDS)
    ap.add_argument("--years", type=int, default=DEFAULT_YEARS)
    ap.add_argument("--json", type=str, default=None, help="write results as JSON")
    args = ap.parse_args()

    n = args.years * TICKS_PER_YEAR

    print("# Nexus 4 -- Leak-Blindness Experiment\n")
    print(f"- script version: `{SCRIPT_VERSION}`")
    print(f"- python: `{platform.python_version()}`  numpy: `{np.__version__}`")
    print(f"- run length: {args.years} years at {TICKS_PER_YEAR} ticks/year "
          f"= {n} ticks")
    print(f"- noise sigma: {SIGMA}   excursion amplitude: {AMPLITUDE} sigma")
    print(f"- calibration: every detector tuned to <= {TARGET_FALSE_ALARM:.0%} "
          f"false-alarm probability on the null over {args.calib_seeds} runs")
    print(f"- evaluation seeds per condition: {args.seeds}\n")

    print("## Self-tests\n")
    for m in run_self_tests(n):
        print(f"- {m}")
    print()

    dets = build_detectors()

    print("## Calibrated thresholds\n")
    print("| detector | threshold h | null false-alarm |")
    print("|---|---|---|")
    for d in dets:
        d.h = calibrate(d, n, args.calib_seeds, TARGET_FALSE_ALARM)
        fa = _null_fa(d, n, args.calib_seeds, d.h)
        print(f"| {d.label} | {d.h:.4f} | {fa:.3f} |")
    print()

    results: dict[str, dict] = {}
    for d in dets:
        results[d.key] = {k: evaluate(d, k, n, args.seeds) for k in SIGNAL_KINDS}

    print("## Fire rate by condition\n")
    print("| detector | null | creep | instrument | greensky | shock | confound |")
    print("|---|---|---|---|---|---|---|")
    for d in dets:
        r = results[d.key]
        cells = " | ".join(f"{r[k]['fire_rate']:.2f}" for k in SIGNAL_KINDS)
        print(f"| {d.label} | {cells} |")
    print()

    print("## Detection delay on the creep condition (years after onset)\n")
    print("| detector | median delay | detected within run |")
    print("|---|---|---|")
    for d in dets:
        r = results[d.key]["creep"]
        md = r["median_delay_years"]
        print(f"| {d.label} | {'n/a' if md is None else f'{md:.1f}'} "
              f"| {r['detected_before_end']:.2f} |")
    print()

    print("## Green Sky reversal behaviour\n")
    print("| detector | latched during green | cleared after return | "
          "still alarming after return |")
    print("|---|---|---|---|")
    for d in dets:
        r = results[d.key]["greensky"]
        if "latched_fraction_of_green" not in r:
            continue
        print(f"| {d.label} | {r['latched_fraction_of_green']:.2f} "
              f"| {r['cleared_after_return']:.2f} "
              f"| {r['still_alarming_after_return']:.2f} |")
    print()

    print("## Minimum detectable drift rate (sigma per year, lower is better)\n")
    mdr = {}
    for d in dets:
        mdr[d.key] = min_detectable_rate(d, n, max(6, args.seeds // 3))
    print("| detector | min detectable rate | years to accumulate 1 sigma |")
    print("|---|---|---|")
    for d in dets:
        v = mdr[d.key]
        print(f"| {d.label} | {'none' if v is None else f'{v:.5f}'} "
              f"| {'n/a' if v is None else f'{1.0 / v:.0f}'} |")
    print()

    print("## Horizon robustness "
          "(null false-alarm rate at longer horizons, same threshold)\n")
    print("A detector calibrated at 1x should still hold at 4x and 16x. If the "
          "false-alarm rate climbs, the detector's calibration depends on "
          "knowing the run length in advance -- which a 10,000-year individual "
          "does not.\n")
    hz = {}
    print("| detector | 1x | 4x | 16x |")
    print("|---|---|---|---|")
    for d in dets:
        hz[d.key] = horizon_robustness(d, n, max(6, args.seeds // 3))
        print(f"| {d.label} | {hz[d.key]['x1']:.2f} | {hz[d.key]['x4']:.2f} "
              f"| {hz[d.key]['x16']:.2f} |")
    print()

    print("## Pre-registered predictions\n")
    checks = check_predictions(results, mdr)
    print("| id | kind | verdict | statement |")
    print("|---|---|---|---|")
    pred_map = {p[0]: p for p in PREDICTIONS}
    for c in checks:
        pid = c["id"]
        print(f"| {pid} | {pred_map[pid][1]} | **{c['verdict']}** | "
              f"{pred_map[pid][2]} |")
    print("\n### Evidence\n")
    for c in checks:
        print(f"- **{c['id']} {c['verdict']}** -- {c['evidence']}")
    print()

    n_fail = sum(1 for c in checks if c["verdict"] == "FAIL")
    print(f"**{len(checks) - n_fail}/{len(checks)} predictions held. "
          f"{n_fail} falsified.**\n")

    if args.json:
        payload = {
            "script_version": SCRIPT_VERSION,
            "python": platform.python_version(),
            "numpy": np.__version__,
            "config": {"years": args.years, "ticks_per_year": TICKS_PER_YEAR,
                       "n": n, "sigma": SIGMA, "amplitude": AMPLITUDE,
                       "seeds": args.seeds, "calib_seeds": args.calib_seeds,
                       "target_false_alarm": TARGET_FALSE_ALARM},
            "thresholds": {d.key: d.h for d in dets},
            "results": results,
            "min_detectable_rate": mdr,
            "horizon_robustness": hz,
            "predictions": [{"id": p[0], "kind": p[1], "statement": p[2]}
                            for p in PREDICTIONS],
            "prediction_checks": checks,
        }
        with open(args.json, "w") as f:
            json.dump(payload, f, indent=2)
        print(f"JSON written to {args.json}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
