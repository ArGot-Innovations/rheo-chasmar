#!/usr/bin/env python3
"""
nexus4_leak_blindness_v2_0.py
==============================

Project Nexus 4 -- Objective C slow-drift / deep-time detector experiment.

STATUS
------
RESEARCH / EXPERIMENTAL. Not canon. Not a Nexus specification.

PURPOSE
-------
This version merges the strongest parts of three earlier experiment lines:

1. the original Green-Sky / world-vs-instrument / shock / confound generator;
2. vectorized detector statistics and one-pass empirical calibration;
3. explicit scope guardrails, pre/post-onset metrics, exact leaky-memory controls;
4. horizon-robustness testing added after the first pilot exposed horizon dependence;
5. an anytime-valid Gaussian-mixture e-process control so "survived 16x" is not
   confused with "valid for an unknown/unbounded horizon".

The experiment does NOT claim that all Nexus stability barriers are leaky, that
THDE reduces to one scalar recurrence, or that any candidate detector here is
canonical. HVD 1.5 only requires TMS to preserve sufficient trajectory/history
for a future controller to compute something *such as* a leaky recurrence, while
the broader Nexus architecture also contains rate-independent hysteresis.

QUESTIONS
---------
A. Finite-horizon behavior:
   How do candidate detector classes behave on stationary noise, gradual world
   displacement, instrument drift, Green-Sky reversal, fast shock, and a
   world/instrument confound?

B. Deep-time calibration:
   If a detector is tuned at a 1050-year horizon and then left unchanged, how
   does its null false-alarm probability behave at 4x and 16x that horizon?

C. Leaky-memory mathematics:
   What properties follow exactly from q[k+1] = lambda*q[k] + s under constant
   input, and what properties follow from a normalized linear EWMA? These are
   analytic controls, not claims about Nexus's real severity mapping.

D. Identifiability:
   If world drift and instrument drift are constructed to produce bit-identical
   channel-1 observations, can any single-channel detector identify the cause?

E. Reference semantics:
   How does a fixed original reference differ from a bank that already contains
   a previously retained Green-Sky epoch? The latter is an explicit recurrence
   comparator and MUST NOT be interpreted as solving first-time reference
   authorization or migration.

DEPENDENCIES
------------
Python 3.10+, NumPy. No network, plotting, SciPy, or optional execution path.

DETERMINISM
-----------
Fixed seed families. Same Python/NumPy versions should reproduce the numerical
results closely; the script records its own SHA-256 in JSON output.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

import numpy as np

SCRIPT_VERSION = "2.0.0-merged-audited"

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

TICKS_PER_YEAR = 12
BLUE_YEARS = 500
TRANS_YEARS = 150
GREEN_YEARS = 150
TAIL_YEARS = 100
DEFAULT_YEARS = BLUE_YEARS + TRANS_YEARS + GREEN_YEARS + TRANS_YEARS + TAIL_YEARS

SIGMA = 1.0
AMPLITUDE = 6.0
TARGET_FALSE_ALARM = 0.05
DEFAULT_CALIB_SEEDS = 200
DEFAULT_EVAL_SEEDS = 40
DEFAULT_MDR_SEEDS = 16
DEFAULT_HORIZON_SEEDS = 40
HORIZON_FACTORS = (1, 4, 16)

# Gaussian-mixture e-process tuning parameter. Under iid N(0,1) null,
# M_t = sqrt(rho/(rho+t))*exp(S_t^2/(2(rho+t))) is a nonnegative martingale.
# Ville's inequality gives P(sup_t M_t >= 1/alpha) <= alpha.
E_RHO = 100.0

# Seed namespaces are deliberately disjoint.
SEED_CALIB = 90_000
SEED_EVAL = 1_000
SEED_MDR = 5_000
SEED_HORIZON = 77_000


# ---------------------------------------------------------------------------
# Signal generation
# ---------------------------------------------------------------------------

@dataclass
class Signal:
    name: str
    x: np.ndarray
    x2: np.ndarray | None = None
    world: np.ndarray | None = None
    bias: np.ndarray | None = None
    events: dict[str, int] = field(default_factory=dict)
    note: str = ""


def _noise(rng: np.random.Generator, n: int) -> np.ndarray:
    return rng.normal(0.0, SIGMA, size=n)


def make_signal(kind: str, seed: int, n: int) -> Signal:
    """Build one observation stream.

    `creep` and `instrument` are intentionally bit-identical on channel 1.
    Different latent causes + identical observations make single-channel causal
    attribution impossible by construction.
    """
    rng = np.random.default_rng(seed)
    eps = _noise(rng, n)
    zeros = np.zeros(n, dtype=np.float64)
    t = np.arange(n)

    onset = BLUE_YEARS * TICKS_PER_YEAR
    up_end = onset + TRANS_YEARS * TICKS_PER_YEAR
    plateau_end = up_end + GREEN_YEARS * TICKS_PER_YEAR
    down_end = plateau_end + TRANS_YEARS * TICKS_PER_YEAR
    rate = AMPLITUDE / (TRANS_YEARS * TICKS_PER_YEAR)

    ramp = np.clip((t - onset) * rate, 0.0, AMPLITUDE)
    eps2 = _noise(np.random.default_rng(seed + 10**6), n)

    if kind == "null":
        return Signal(
            "null", eps, x2=eps2, world=zeros, bias=zeros,
            note="stationary noise; no world change and no instrument drift",
        )

    if kind == "creep":
        return Signal(
            "creep", ramp + eps, x2=ramp + eps2,
            world=ramp, bias=zeros, events={"onset": onset},
            note="world state gradually moves; both instruments agree",
        )

    if kind == "instrument":
        return Signal(
            "instrument", ramp + eps, x2=eps2,
            world=zeros, bias=ramp, events={"onset": onset},
            note="instrument 1 drifts; world and instrument 2 remain stable",
        )

    if kind == "greensky":
        back = np.clip((t - plateau_end) * rate, 0.0, AMPLITUDE)
        world = ramp - back
        return Signal(
            "greensky", world + eps, x2=world + eps2,
            world=world, bias=zeros,
            events={
                "onset": onset,
                "plateau_start": up_end,
                "reversal": plateau_end,
                "settled": down_end,
            },
            note="blue -> gradual green -> green plateau -> gradual blue -> blue",
        )

    if kind == "shock":
        world = np.where(t >= onset, AMPLITUDE, 0.0)
        return Signal(
            "shock", world + eps, x2=world + eps2,
            world=world, bias=zeros, events={"onset": onset},
            note="common-mode step change in world state",
        )

    if kind == "confound":
        # Channel 1: world +3 and instrument bias -3 cancel exactly.
        # Channel 2: independent instrument sees world +3.
        half = ramp / 2.0
        return Signal(
            "confound", eps, x2=half + eps2,
            world=half, bias=-half, events={"onset": onset},
            note="world and instrument-1 drift cancel on ch1; ch2 sees world drift",
        )

    raise ValueError(f"unknown signal kind: {kind}")


SIGNAL_KINDS = ("null", "creep", "instrument", "greensky", "shock", "confound")


# ---------------------------------------------------------------------------
# Detector statistics
# ---------------------------------------------------------------------------


def d_leaky_abs(
    x: np.ndarray,
    h: float | None = None,
    lam: float = 0.99,
    mu: float = 0.0,
) -> np.ndarray:
    """q[k] = lam*q[k-1] + |x[k]-mu|.

    Candidate scalar analog only. This MUST NOT be equated with the complete
    THDE runtime or with all Nexus hysteresis operators.
    """
    sev = np.abs(x - mu)
    stat = np.empty(len(x), dtype=np.float64)
    q = 0.0
    for k, value in enumerate(sev):
        q = lam * q + float(value)
        stat[k] = q
    return stat if h is None else stat >= h


def d_raw_fixed_abs(
    x: np.ndarray,
    h: float | None = None,
    mu: float = 0.0,
) -> np.ndarray:
    stat = np.cumsum(np.abs(x - mu))
    return stat if h is None else stat >= h


def d_raw_sqrt(
    x: np.ndarray,
    h: float | None = None,
    mu: float = 0.0,
) -> np.ndarray:
    """|S_k|/sqrt(k), retained as the legacy finite-horizon comparator.

    It is NOT anytime-valid: under an iid mean-zero random walk, the law of the
    iterated logarithm implies eventual excursions beyond every fixed c*sqrt(k)
    boundary with probability one.
    """
    s = np.cumsum(x - mu)
    stat = np.abs(s) / np.sqrt(np.arange(1, len(x) + 1, dtype=np.float64))
    return stat if h is None else stat >= h


def d_cusum1(
    x: np.ndarray,
    h: float | None = None,
    nu: float = 0.5,
    mu: float = 0.0,
) -> np.ndarray:
    """One-sided Page CUSUM via the exact cumulative-sum identity."""
    w = (x - mu) - nu
    s = np.empty(len(x) + 1, dtype=np.float64)
    s[0] = 0.0
    np.cumsum(w, out=s[1:])
    stat = s[1:] - np.minimum.accumulate(s)[1:]
    return stat if h is None else stat >= h


def d_cusum2(
    x: np.ndarray,
    h: float | None = None,
    nu: float = 0.1,
    mu: float = 0.0,
) -> np.ndarray:
    """Two-sided scalar Page CUSUM.

    This is a generic signed-scalar comparator. It is NOT asserted to be the
    correct representation for non-scalar sky color or high-dimensional Nexus
    state.
    """
    r = x - mu

    sp = np.empty(len(x) + 1, dtype=np.float64)
    sp[0] = 0.0
    np.cumsum(r - nu, out=sp[1:])
    cp = sp[1:] - np.minimum.accumulate(sp)[1:]

    sn = np.empty(len(x) + 1, dtype=np.float64)
    sn[0] = 0.0
    np.cumsum(-r - nu, out=sn[1:])
    cn = sn[1:] - np.minimum.accumulate(sn)[1:]

    stat = np.maximum(cp, cn)
    return stat if h is None else stat >= h


def d_refdistance(
    x: np.ndarray,
    h: float | None = None,
    tau: float = 240.0,
    refs: tuple[float, ...] = (0.0,),
) -> np.ndarray:
    """EWMA distance from the nearest FIXED supplied epoch reference.

    No reference is learned or promoted here. If refs=(0,6), the experiment is
    explicitly assuming both epochs are already retained/authorized.
    """
    alpha = 1.0 / tau
    m = np.empty(len(x), dtype=np.float64)
    curr = float(x[0])
    for k, value in enumerate(x):
        curr += alpha * (float(value) - curr)
        m[k] = curr
    ref_arr = np.asarray(refs, dtype=np.float64)
    stat = np.min(np.abs(m[:, None] - ref_arr[None, :]), axis=1)
    return stat if h is None else stat >= h


def d_crosschannel(
    x: np.ndarray,
    x2: np.ndarray,
    h: float | None = None,
    tau: float = 240.0,
) -> np.ndarray:
    """EWMA of channel disagreement.

    This detects disagreement/common-mode cancellation structure. It does not
    prove which instrument is truthful without independent metrological or
    provenance assumptions.
    """
    alpha = 1.0 / tau
    diff = x - x2
    stat = np.empty(len(diff), dtype=np.float64)
    curr = 0.0
    for k, value in enumerate(diff):
        curr += alpha * (float(value) - curr)
        stat[k] = abs(curr)
    return stat if h is None else stat >= h


def d_normal_mixture_e(
    x: np.ndarray,
    h: float | None = None,
    mu: float = 0.0,
    sigma: float = SIGMA,
    rho: float = E_RHO,
) -> np.ndarray:
    """Two-sided Gaussian normal-mixture e-process log statistic.

    Under iid N(mu, sigma^2) observations with known sigma,

        M_t = sqrt(rho/(rho+t)) * exp(S_t^2 / (2*(rho+t)))

    for S_t = sum((x_i-mu)/sigma) is a nonnegative martingale under the null.
    Alarm at log(M_t) >= log(1/alpha). Ville's inequality gives a time-uniform
    false-alarm bound <= alpha for the modeled null.

    This is a CONTROL demonstrating the distinction between empirical
    fixed-horizon calibration and an anytime-valid sequential boundary. It is
    not proposed as canonical Nexus machinery.
    """
    z = (x - mu) / sigma
    s = np.cumsum(z)
    t = np.arange(1, len(x) + 1, dtype=np.float64)
    log_m = 0.5 * (math.log(rho) - np.log(rho + t)) + (s * s) / (2.0 * (rho + t))
    return log_m if h is None else log_m >= h


# Sequential references for vectorization self-tests.
def _ref_cusum1(x: np.ndarray, h: float, nu: float, mu: float = 0.0) -> np.ndarray:
    c = 0.0
    out = np.empty(len(x), dtype=bool)
    for k, value in enumerate(x):
        c = max(0.0, c + (float(value) - mu) - nu)
        out[k] = c >= h
    return out


def _ref_cusum2(x: np.ndarray, h: float, nu: float, mu: float = 0.0) -> np.ndarray:
    cp = 0.0
    cn = 0.0
    out = np.empty(len(x), dtype=bool)
    for k, value in enumerate(x):
        r = float(value) - mu
        cp = max(0.0, cp + r - nu)
        cn = max(0.0, cn - r - nu)
        out[k] = (cp >= h) or (cn >= h)
    return out


# ---------------------------------------------------------------------------
# Detector registry
# ---------------------------------------------------------------------------

@dataclass
class Detector:
    key: str
    label: str
    fn: Callable
    kwargs: dict = field(default_factory=dict)
    two_channel: bool = False
    threshold_mode: str = "empirical_fixed_horizon"  # or analytic_anytime
    h: float = float("nan")


def build_detectors(alpha: float = TARGET_FALSE_ALARM) -> list[Detector]:
    dets: list[Detector] = []
    for lam in (0.90, 0.99, 0.999):
        tau = 1.0 / (1.0 - lam)
        dets.append(Detector(
            f"leaky_l{lam}",
            f"Leaky absolute-deviation accumulator, lambda={lam} (tau={tau:.0f})",
            d_leaky_abs,
            {"lam": lam},
        ))

    dets.extend([
        Detector("raw_fixed", "Raw absolute-deviation sum, fixed threshold", d_raw_fixed_abs),
        Detector("raw_sqrt", "Centered cumulative sum / sqrt(k) [legacy]", d_raw_sqrt),
        Detector("cusum1_v0.5", "One-sided CUSUM, nu=0.5", d_cusum1, {"nu": 0.5}),
        Detector("cusum1_v0.1", "One-sided CUSUM, nu=0.1", d_cusum1, {"nu": 0.1}),
        Detector("cusum1_v0.02", "One-sided CUSUM, nu=0.02", d_cusum1, {"nu": 0.02}),
        Detector("cusum2_v0.1", "Two-sided scalar CUSUM, nu=0.1", d_cusum2, {"nu": 0.1}),
        Detector(
            "ref_blue",
            "Fixed-reference EWMA distance [blue only]",
            d_refdistance,
            {"refs": (0.0,)},
        ),
        Detector(
            "ref_blue_green_known",
            "Known-epoch EWMA bank [blue+green already retained]",
            d_refdistance,
            {"refs": (0.0, AMPLITUDE)},
        ),
        Detector(
            "crosschannel",
            "Cross-channel disagreement EWMA",
            d_crosschannel,
            two_channel=True,
        ),
        Detector(
            "normal_mixture_e",
            f"Gaussian-mixture e-process, alpha={alpha}",
            d_normal_mixture_e,
            {"rho": E_RHO},
            threshold_mode="analytic_anytime",
            h=math.log(1.0 / alpha),
        ),
    ])
    return dets


def _detector_stat(det: Detector, sig: Signal) -> np.ndarray:
    if det.two_channel:
        if sig.x2 is None:
            raise ValueError(f"{det.key} requires channel 2")
        return det.fn(sig.x, sig.x2, None, **det.kwargs)
    return det.fn(sig.x, None, **det.kwargs)


def _detector_alarm(det: Detector, sig: Signal, h: float | None = None) -> np.ndarray:
    threshold = det.h if h is None else h
    if det.two_channel:
        if sig.x2 is None:
            raise ValueError(f"{det.key} requires channel 2")
        return det.fn(sig.x, sig.x2, threshold, **det.kwargs)
    return det.fn(sig.x, threshold, **det.kwargs)


# ---------------------------------------------------------------------------
# Calibration
# ---------------------------------------------------------------------------


def empirical_calibrate(det: Detector, n: int, seeds: int, target_fa: float) -> float:
    """Calibrate from per-run null maxima computed once.

    The threshold is chosen just above the order statistic that permits at most
    floor(target_fa * seeds) calibration runs to alarm. This makes the finite
    seed quantization explicit and avoids re-running detectors during bisection.
    """
    maxima = np.empty(seeds, dtype=np.float64)
    for s in range(seeds):
        sig = make_signal("null", SEED_CALIB + s, n)
        maxima[s] = float(np.max(_detector_stat(det, sig)))

    allowed_hits = int(math.floor(target_fa * seeds))
    sorted_max = np.sort(maxima)
    if allowed_hits >= seeds:
        return float(np.nextafter(sorted_max[0], -np.inf))
    boundary_index = seeds - allowed_hits - 1
    return float(np.nextafter(sorted_max[boundary_index], np.inf))


def calibrate_detectors(dets: list[Detector], n: int, seeds: int, alpha: float) -> dict:
    info = {}
    for det in dets:
        if det.threshold_mode == "empirical_fixed_horizon":
            det.h = empirical_calibrate(det, n, seeds, alpha)
        elif det.threshold_mode == "analytic_anytime":
            # h pre-populated from the mathematical guarantee.
            pass
        else:
            raise ValueError(f"unknown threshold mode: {det.threshold_mode}")

        fa = null_false_alarm(det, n, seeds, SEED_CALIB)
        info[det.key] = {
            "threshold": det.h,
            "threshold_mode": det.threshold_mode,
            "calibration_null_fa": fa,
        }
    return info


def null_false_alarm(det: Detector, n: int, seeds: int, seed_base: int) -> float:
    hits = 0
    for s in range(seeds):
        sig = make_signal("null", seed_base + s, n)
        if _detector_alarm(det, sig).any():
            hits += 1
    return hits / seeds


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------


def first_alarm_from(a: np.ndarray, start: int) -> int | None:
    idx = np.flatnonzero(a[start:])
    return int(start + idx[0]) if idx.size else None


def evaluate_condition(det: Detector, kind: str, n: int, seeds: int) -> dict:
    any_alarm = 0
    pre_onset_alarm = 0
    post_onset_detect = 0
    delays: list[float] = []
    plateau_alarm_fraction: list[float] = []
    quiet_after_return = 0
    alarm_after_return = 0

    for s in range(seeds):
        sig = make_signal(kind, SEED_EVAL + s, n)
        a = _detector_alarm(det, sig)

        if a.any():
            any_alarm += 1

        onset = sig.events.get("onset")
        if onset is not None:
            if a[:onset].any():
                pre_onset_alarm += 1
            post = first_alarm_from(a, onset)
            if post is not None:
                post_onset_detect += 1
                delays.append((post - onset) / TICKS_PER_YEAR)

        ps = sig.events.get("plateau_start")
        rev = sig.events.get("reversal")
        settled = sig.events.get("settled")
        if ps is not None and rev is not None and settled is not None:
            plateau = a[ps:rev]
            plateau_alarm_fraction.append(float(plateau.mean()) if plateau.size else 0.0)
            tail = a[settled:]
            if tail.any():
                alarm_after_return += 1
            else:
                quiet_after_return += 1

    out = {
        "any_alarm_rate": any_alarm / seeds,
        "pre_onset_false_alarm_rate": None,
        "post_onset_detection_rate": None,
        "median_post_onset_delay_years": None,
    }
    if kind != "null":
        out["pre_onset_false_alarm_rate"] = pre_onset_alarm / seeds
        out["post_onset_detection_rate"] = post_onset_detect / seeds
        if delays:
            out["median_post_onset_delay_years"] = float(np.median(delays))

    if plateau_alarm_fraction:
        out["plateau_alarm_fraction"] = float(np.mean(plateau_alarm_fraction))
        out["quiet_after_return_rate"] = quiet_after_return / seeds
        out["alarm_after_return_rate"] = alarm_after_return / seeds

    return out


def horizon_robustness(
    det: Detector,
    base_n: int,
    seeds: int,
    factors: tuple[int, ...] = HORIZON_FACTORS,
) -> dict[str, float]:
    """Reuse the base-horizon threshold at longer null horizons.

    One max-length null trace is generated per seed; alarms are then checked on
    prefixes. This is faster and makes x1/x4/x16 nested for each seed.
    """
    max_factor = max(factors)
    hits = {f: 0 for f in factors}
    max_n = base_n * max_factor

    for s in range(seeds):
        sig = make_signal("null", SEED_HORIZON + s, max_n)
        a = _detector_alarm(det, sig)
        for f in factors:
            if a[: base_n * f].any():
                hits[f] += 1

    return {f"x{f}": hits[f] / seeds for f in factors}


def min_detectable_ramp_rate(
    det: Detector,
    n: int,
    seeds: int,
    power: float = 0.50,
) -> float | None:
    """Legacy finite-horizon linear-ramp sensitivity metric.

    Alternative starts at tick 0: x_k = k*rate + noise. This is a STATE
    displacement ramp, not a derivative-only severity stream. Because final
    displacement grows with horizon, this metric cannot by itself establish an
    asymptotic leaky-memory floor.
    """
    if det.two_channel:
        return None

    def catches(rate_per_year: float) -> bool:
        hits = 0
        rate_per_tick = rate_per_year / TICKS_PER_YEAR
        trend = np.arange(n, dtype=np.float64) * rate_per_tick
        for s in range(seeds):
            rng = np.random.default_rng(SEED_MDR + s)
            x = trend + rng.normal(0.0, SIGMA, n)
            sig = Signal("mdr", x)
            if _detector_alarm(det, sig).any():
                hits += 1
        return hits / seeds >= power

    lo, hi = 1e-7, 1.0
    if not catches(hi):
        return None
    for _ in range(24):
        mid = math.sqrt(lo * hi)
        if catches(mid):
            hi = mid
        else:
            lo = mid
    return hi


# ---------------------------------------------------------------------------
# Analytic controls
# ---------------------------------------------------------------------------


def leaky_fixed_point_control() -> list[dict]:
    """Exact constant-severity property of q[k+1]=lambda*q[k]+s.

    q_inf = s/(1-lambda). For threshold theta, constant s below
    (1-lambda)*theta never reaches theta in the idealized recurrence.
    """
    theta = 1.0
    rows = []
    for lam in (0.90, 0.99, 0.999):
        floor = (1.0 - lam) * theta
        rows.append({
            "lambda": lam,
            "theta": theta,
            "crossing_floor_severity": floor,
            "below_severity": 0.5 * floor,
            "below_q_infinity": 0.5,
            "above_severity": 1.5 * floor,
            "above_q_infinity": 1.5,
        })
    return rows


def leaky_effective_memory_control() -> list[dict]:
    """Exact variance floor for a normalized LINEAR EWMA control.

    m_k = lambda*m_{k-1} + (1-lambda)*x_k, x_k iid with variance sigma^2.

    Var(m_inf) = sigma^2 * (1-lambda)/(1+lambda)
    N_eff       = (1+lambda)/(1-lambda)

    This demonstrates finite effective memory for a linear centered leaky
    estimator. It does NOT assert that THDE's real severity mapping is linear,
    signed, Gaussian, scalar, or identical to this control.
    """
    rows = []
    for lam in (0.90, 0.99, 0.999):
        n_eff = (1.0 + lam) / (1.0 - lam)
        sd_floor = SIGMA * math.sqrt((1.0 - lam) / (1.0 + lam))
        rows.append({
            "lambda": lam,
            "tau_1_over_1_minus_lambda": 1.0 / (1.0 - lam),
            "effective_sample_size": n_eff,
            "stationary_sd": sd_floor,
        })
    return rows


# ---------------------------------------------------------------------------
# Historical predictions and post-pilot replication targets
# ---------------------------------------------------------------------------

# These eight statements are preserved verbatim from the pre-pilot experiment.
# P3, P4, and P5 were falsified. They are historical record, not editable truth.
LEGACY_HISTORICAL_VERDICTS = {
    "P1": "PASS",
    "P2": "PASS",
    "P3": "FAIL",
    "P4": "FAIL",
    "P5": "FAIL",
    "P6": "PASS",
    "P7": "PASS",
    "P8": "PASS",
}

LEGACY_PREDICTIONS = [
    ("P1", "analytic",
     "Leaky detectors have a minimum-detectable-rate at least 3x worse than raw_sqrt, and it does NOT improve as lambda->1 fast enough to close the gap."),
    ("P2", "empirical",
     "Every detector fires on the SHOCK condition. Fast shocks are not the problem."),
    ("P3", "analytic",
     "raw_fixed cannot be calibrated: it either alarms on the null or never alarms at all. It measures elapsed time, not departure."),
    ("P4", "empirical",
     "CUSUM with nu=0.5 is blind to the Green Sky drift rate (fire_rate < 0.5 on 'creep'). CUSUM does not automatically fix slow drift; nu is a floor."),
    ("P5", "empirical",
     "raw_sqrt has the lowest minimum-detectable-rate of all single-channel detectors tested."),
    ("P6", "empirical",
     "With a FIXED reference, at least one detector stays latched for >50% of the green plateau -- i.e. it spends 150 years reporting that a genuinely green sky is anomalous."),
    ("P7", "analytic",
     "Conditions 'creep' and 'instrument' produce identical channel-1 streams, so every single-channel detector gives identical results on both. Integral tracking alone cannot solve the instrument problem."),
    ("P8", "empirical",
     "The cross-channel detector fires on 'instrument' and NOT on 'creep', separating world change from instrument change."),
]

# Registered AFTER the v1.1 pilot and therefore not evidence of pre-pilot novelty.
# They are useful independent-replication targets for v2.0.
POST_PILOT_TARGETS = [
    ("R1", "post-pilot replication",
     "raw_fixed loses fixed-horizon calibration badly by x4 (null FA >= 0.50)."),
    ("R2", "post-pilot replication",
     "CUSUM nu=0.5 detects the configured 6-sigma creep excursion (post-onset detection >= 0.90)."),
    ("R3", "post-pilot replication",
     "raw_sqrt and CUSUM nu=0.02 have finite-horizon MDR50 values within a factor of 2."),
    ("R4", "new control",
     "The Gaussian-mixture e-process remains <=10% empirical null FA at every tested horizon x1/x4/x16."),
    ("R5", "post-pilot replication",
     "Cross-channel disagreement is low on common-mode creep (<=0.10) and high on instrument drift and confound (>=0.90 each)."),
    ("R6", "reference semantics",
     "The blue-only reference alarms for most of the green plateau, while the pre-known blue+green bank alarms for substantially less of that plateau."),
]


def check_legacy_predictions(results: dict, mdr: dict) -> list[dict]:
    out = []

    def rec(pid: str, verdict: str, evidence: str) -> None:
        out.append({"id": pid, "verdict": verdict, "evidence": evidence})

    leaky = [mdr[k] for k in ("leaky_l0.9", "leaky_l0.99", "leaky_l0.999") if mdr.get(k)]
    sq = mdr.get("raw_sqrt")
    if leaky and sq:
        best_leaky = min(leaky)
        ratio = best_leaky / sq
        rec("P1", "PASS" if ratio >= 3.0 else "FAIL",
            f"best leaky MDR={best_leaky:.8g}; raw_sqrt={sq:.8g}; ratio={ratio:.2f}x")
    else:
        rec("P1", "INDETERMINATE", "missing MDR data")

    shock = {k: v["shock"]["post_onset_detection_rate"] for k, v in results.items()}
    # Historical check explicitly excludes the cross-channel common-mode detector.
    eligible = {k: v for k, v in shock.items() if k != "crosschannel"}
    rec("P2", "PASS" if all(v is not None and v >= 0.95 for v in eligible.values()) else "FAIL",
        f"post-onset shock detection: {eligible}")

    rf_null = results["raw_fixed"]["null"]["any_alarm_rate"]
    rf_creep = results["raw_fixed"]["creep"]["post_onset_detection_rate"]
    rec("P3", "PASS" if rf_null > 0.5 or (rf_creep is not None and rf_creep < 0.5) else "FAIL",
        f"raw_fixed null any-alarm={rf_null}; creep post-onset detection={rf_creep}")

    c05 = results["cusum1_v0.5"]["creep"]["post_onset_detection_rate"]
    rec("P4", "PASS" if c05 is not None and c05 < 0.5 else "FAIL",
        f"CUSUM nu=0.5 creep post-onset detection={c05}")

    single = {k: v for k, v in mdr.items() if v is not None and k != "crosschannel"}
    best = min(single, key=single.get) if single else None
    rec("P5", "PASS" if best == "raw_sqrt" else "FAIL",
        f"lowest finite-horizon MDR is {best}={single.get(best) if best else None}; raw_sqrt={sq}")

    plateau = {
        k: v["greensky"].get("plateau_alarm_fraction")
        for k, v in results.items()
        if k not in ("crosschannel", "ref_blue_green_known")
    }
    worst = max(v for v in plateau.values() if v is not None)
    rec("P6", "PASS" if worst > 0.5 else "FAIL",
        f"max green-plateau alarm fraction={worst}; {plateau}")

    # Compare only single-channel detectors. x is bit-identical by construction.
    single_keys = [k for k in results if k != "crosschannel"]
    same = all(results[k]["creep"] == results[k]["instrument"] for k in single_keys)
    rec("P7", "PASS" if same else "FAIL",
        "single-channel result dictionaries identical" if same else "unexpected mismatch")

    cc_inst = results["crosschannel"]["instrument"]["post_onset_detection_rate"]
    cc_creep = results["crosschannel"]["creep"]["post_onset_detection_rate"]
    rec("P8", "PASS" if cc_inst >= 0.9 and cc_creep <= 0.1 else "FAIL",
        f"crosschannel instrument={cc_inst}; creep={cc_creep}")
    return out


def check_post_pilot_targets(results: dict, mdr: dict, hz: dict) -> list[dict]:
    out = []

    def rec(pid: str, verdict: str, evidence: str) -> None:
        out.append({"id": pid, "verdict": verdict, "evidence": evidence})

    rf_x4 = hz["raw_fixed"]["x4"]
    rec("R1", "PASS" if rf_x4 >= 0.50 else "FAIL", f"raw_fixed x4 null FA={rf_x4}")

    c05 = results["cusum1_v0.5"]["creep"]["post_onset_detection_rate"]
    rec("R2", "PASS" if c05 >= 0.90 else "FAIL", f"CUSUM nu=0.5 creep detection={c05}")

    a = mdr.get("raw_sqrt")
    b = mdr.get("cusum1_v0.02")
    if a and b:
        ratio = max(a, b) / min(a, b)
        rec("R3", "PASS" if ratio <= 2.0 else "FAIL",
            f"raw_sqrt={a:.8g}; CUSUM.02={b:.8g}; ratio={ratio:.2f}")
    else:
        rec("R3", "INDETERMINATE", "missing MDR data")

    e_hz = hz["normal_mixture_e"]
    rec("R4", "PASS" if all(v <= 0.10 for v in e_hz.values()) else "FAIL",
        f"Gaussian-mixture e-process horizon FA={e_hz}")

    cc_creep = results["crosschannel"]["creep"]["post_onset_detection_rate"]
    cc_inst = results["crosschannel"]["instrument"]["post_onset_detection_rate"]
    cc_conf = results["crosschannel"]["confound"]["post_onset_detection_rate"]
    ok = cc_creep <= 0.10 and cc_inst >= 0.90 and cc_conf >= 0.90
    rec("R5", "PASS" if ok else "FAIL",
        f"crosschannel creep={cc_creep}, instrument={cc_inst}, confound={cc_conf}")

    blue = results["ref_blue"]["greensky"]["plateau_alarm_fraction"]
    known = results["ref_blue_green_known"]["greensky"]["plateau_alarm_fraction"]
    rec("R6", "PASS" if blue >= 0.80 and known <= blue - 0.30 else "FAIL",
        f"blue-only plateau alarm={blue:.3f}; known blue+green={known:.3f}")
    return out


# ---------------------------------------------------------------------------
# Self-tests and provenance
# ---------------------------------------------------------------------------


def run_self_tests(n: int) -> list[str]:
    if n < DEFAULT_YEARS * TICKS_PER_YEAR:
        raise ValueError(
            f"primary scenario horizon must be >= {DEFAULT_YEARS} years; got {n / TICKS_PER_YEAR}"
        )

    msgs: list[str] = []

    a = make_signal("creep", 7, n)
    b = make_signal("instrument", 7, n)
    assert np.array_equal(a.x, b.x)
    msgs.append("PASS creep and instrument channel-1 streams are bit-identical")

    assert not np.array_equal(a.x2, b.x2)
    msgs.append("PASS creep and instrument channel-2 streams differ")

    g = make_signal("greensky", 7, n)
    assert abs(float(g.world[-1])) < 1e-12
    msgs.append("PASS Green Sky returns exactly to original baseline")

    assert abs(float(g.world.max()) - AMPLITUDE) < 1e-12
    msgs.append("PASS Green Sky reaches configured amplitude")

    ps, rev = g.events["plateau_start"], g.events["reversal"]
    assert np.allclose(g.world[ps:rev], AMPLITUDE)
    msgs.append(f"PASS green plateau is flat for {GREEN_YEARS} years")

    # Vectorized CUSUM identities.
    rng = np.random.default_rng(314159)
    x = rng.normal(0.0, 1.0, 5000)
    for nu in (0.5, 0.1, 0.02):
        h = 7.25
        assert np.array_equal(d_cusum1(x, h, nu=nu), _ref_cusum1(x, h, nu))
    msgs.append("PASS vectorized one-sided CUSUM matches sequential recurrence")

    assert np.array_equal(d_cusum2(x, 7.25, nu=0.1), _ref_cusum2(x, 7.25, 0.1))
    msgs.append("PASS vectorized two-sided CUSUM matches sequential recurrence")

    # Exact e-process first-step formula sanity check.
    one = np.array([0.0])
    logm = d_normal_mixture_e(one, None, rho=E_RHO)
    expected = 0.5 * (math.log(E_RHO) - math.log(E_RHO + 1.0))
    assert abs(float(logm[0]) - expected) < 1e-12
    msgs.append("PASS Gaussian-mixture e-process formula sanity check")

    return msgs


def file_sha256() -> str:
    try:
        return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    except Exception:
        return "UNAVAILABLE"


# ---------------------------------------------------------------------------
# Reporting helpers
# ---------------------------------------------------------------------------


def fmt(v: float | None, digits: int = 3) -> str:
    if v is None:
        return "n/a"
    return f"{v:.{digits}f}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--seeds", type=int, default=DEFAULT_EVAL_SEEDS)
    ap.add_argument("--calib-seeds", type=int, default=DEFAULT_CALIB_SEEDS)
    ap.add_argument("--mdr-seeds", type=int, default=DEFAULT_MDR_SEEDS)
    ap.add_argument("--horizon-seeds", type=int, default=DEFAULT_HORIZON_SEEDS)
    ap.add_argument("--years", type=int, default=DEFAULT_YEARS)
    ap.add_argument("--json", type=str, default=None)
    args = ap.parse_args()

    n = args.years * TICKS_PER_YEAR

    print("# Nexus 4 -- Objective C Deep-Time Detector Experiment v2.0\n")
    print(f"- script version: `{SCRIPT_VERSION}`")
    print(f"- script sha256: `{file_sha256()}`")
    print(f"- python: `{platform.python_version()}`")
    print(f"- numpy: `{np.__version__}`")
    print(f"- primary horizon: {args.years} years = {n} ticks")
    print(f"- evaluation seeds: {args.seeds}")
    print(f"- calibration seeds: {args.calib_seeds}")
    print(f"- MDR seeds: {args.mdr_seeds}")
    print(f"- horizon seeds: {args.horizon_seeds}")
    print(f"- target null false-alarm probability: {TARGET_FALSE_ALARM:.3f}\n")

    print("## Scope guardrails\n")
    print("- RESEARCH artifact, not canon or specification.")
    print("- The leaky absolute-deviation detector is a scalar analog, not the complete THDE runtime.")
    print("- The finite-horizon ramp MDR is not an asymptotic leak-blindness proof.")
    print("- `raw_sqrt` is not anytime-valid despite strong finite tested horizons.")
    print("- The Gaussian-mixture e-process is an anytime-valid control only under its iid Gaussian null assumptions.")
    print("- Cross-channel disagreement does not identify truth without independent reference/provenance.")
    print("- `ref_blue_green_known` assumes both epochs already exist; it does not implement reference authorization/migration.\n")

    print("## Self-tests\n")
    self_tests = run_self_tests(n)
    for row in self_tests:
        print(f"- {row}")
    print()

    dets = build_detectors(TARGET_FALSE_ALARM)
    calibration = calibrate_detectors(dets, n, args.calib_seeds, TARGET_FALSE_ALARM)

    print("## Calibration\n")
    print("| detector | threshold mode | h | base-horizon null FA |")
    print("|---|---|---:|---:|")
    for det in dets:
        c = calibration[det.key]
        print(f"| {det.label} | {c['threshold_mode']} | {c['threshold']:.8g} | {c['calibration_null_fa']:.3f} |")
    print()

    results = {
        det.key: {kind: evaluate_condition(det, kind, n, args.seeds) for kind in SIGNAL_KINDS}
        for det in dets
    }

    print("## Post-onset detection rate by condition\n")
    print("Null column is any-alarm rate because there is no onset.\n")
    print("| detector | null | creep | instrument | greensky | shock | confound |")
    print("|---|---:|---:|---:|---:|---:|---:|")
    for det in dets:
        row = results[det.key]
        vals = [row["null"]["any_alarm_rate"]]
        vals.extend(row[k]["post_onset_detection_rate"] for k in SIGNAL_KINDS[1:])
        print(f"| {det.label} | " + " | ".join(fmt(v, 2) for v in vals) + " |")
    print()

    print("## Creep false alarms and detection delay\n")
    print("| detector | pre-onset FA | post-onset detection | median delay years |")
    print("|---|---:|---:|---:|")
    for det in dets:
        r = results[det.key]["creep"]
        print(
            f"| {det.label} | {fmt(r['pre_onset_false_alarm_rate'],2)} | "
            f"{fmt(r['post_onset_detection_rate'],2)} | {fmt(r['median_post_onset_delay_years'],2)} |"
        )
    print()

    print("## Green Sky reversal behavior\n")
    print("| detector | green plateau alarm fraction | quiet after return | alarm after return |")
    print("|---|---:|---:|---:|")
    for det in dets:
        r = results[det.key]["greensky"]
        print(
            f"| {det.label} | {fmt(r.get('plateau_alarm_fraction'),2)} | "
            f"{fmt(r.get('quiet_after_return_rate'),2)} | {fmt(r.get('alarm_after_return_rate'),2)} |"
        )
    print()

    print("## Finite-horizon minimum detectable linear-ramp rate (MDR50)\n")
    print("Lower is better for THIS configured finite horizon only.\n")
    print("| detector | MDR50 sigma/year | years per 1-sigma displacement |")
    print("|---|---:|---:|")
    mdr: dict[str, float | None] = {}
    for det in dets:
        v = min_detectable_ramp_rate(det, n, args.mdr_seeds, power=0.50)
        mdr[det.key] = v
        if v is None:
            print(f"| {det.label} | n/a | n/a |")
        else:
            print(f"| {det.label} | {v:.8g} | {1.0/v:.0f} |")
    print()

    print("## Horizon robustness: same threshold, longer null horizon\n")
    print("This is a finite stress test at x1/x4/x16, not proof of infinite-horizon validity.\n")
    print("| detector | x1 | x4 | x16 |")
    print("|---|---:|---:|---:|")
    hz = {}
    for det in dets:
        hz[det.key] = horizon_robustness(det, n, args.horizon_seeds)
        print(
            f"| {det.label} | {hz[det.key]['x1']:.2f} | "
            f"{hz[det.key]['x4']:.2f} | {hz[det.key]['x16']:.2f} |"
        )
    print()

    print("## Exact leaky-memory analytic controls\n")
    fixed = leaky_fixed_point_control()
    print("### Constant-severity recurrence\n")
    print("| lambda | threshold | exact severity floor | q_inf at 0.5x floor | q_inf at 1.5x floor |")
    print("|---:|---:|---:|---:|---:|")
    for r in fixed:
        print(
            f"| {r['lambda']:.3f} | {r['theta']:.1f} | {r['crossing_floor_severity']:.6g} | "
            f"{r['below_q_infinity']:.3f} | {r['above_q_infinity']:.3f} |"
        )
    print()

    eff = leaky_effective_memory_control()
    print("### Normalized linear-EWMA effective memory\n")
    print("| lambda | tau=1/(1-lambda) | N_eff=(1+lambda)/(1-lambda) | stationary SD |")
    print("|---:|---:|---:|---:|")
    for r in eff:
        print(
            f"| {r['lambda']:.3f} | {r['tau_1_over_1_minus_lambda']:.1f} | "
            f"{r['effective_sample_size']:.1f} | {r['stationary_sd']:.6f} |"
        )
    print()

    legacy_checks = check_legacy_predictions(results, mdr)
    print("## Historical pre-pilot predictions P1-P8\n")
    print("P3/P4/P5 are intentionally preserved even though earlier pilots falsified them.\n")
    pred_map = {p[0]: p for p in LEGACY_PREDICTIONS}
    print("| id | kind | historical v1.1 verdict | v2.0 rerun verdict | statement |")
    print("|---|---|---|---|---|")
    for c in legacy_checks:
        hist = LEGACY_HISTORICAL_VERDICTS[c["id"]]
        print(f"| {c['id']} | {pred_map[c['id']][1]} | **{hist}** | **{c['verdict']}** | {pred_map[c['id']][2]} |")
    print()

    target_checks = check_post_pilot_targets(results, mdr, hz)
    print("## Post-pilot independent-replication targets R1-R6\n")
    print("These were registered after observing v1.1, so they are replication targets, not pre-pilot discoveries.\n")
    target_map = {p[0]: p for p in POST_PILOT_TARGETS}
    print("| id | class | verdict | target |")
    print("|---|---|---|---|")
    for c in target_checks:
        print(f"| {c['id']} | {target_map[c['id']][1]} | **{c['verdict']}** | {target_map[c['id']][2]} |")
    print()

    print("## Interpretation guardrails\n")
    print("- A finite-horizon detector win does not make that detector canonical Nexus machinery.")
    print("- A fixed threshold that survives x16 has not been proven safe for an unbounded horizon.")
    print("- The e-process has a time-uniform bound only under the modeled iid Gaussian null; model misspecification still matters.")
    print("- `creep` is a growing state displacement, not a direct model of THDE severity_k.")
    print("- The exact q fixed-point control and linear-EWMA variance control are mathematics of simplified recurrences, not evidence about Nexus implementation.")
    print("- The known blue+green reference bank demonstrates retained-epoch recognition only; it does not solve who authorizes a new reference.")
    print("- Cross-channel disagreement establishes identifiability limits and disagreement detection, not absolute truth.\n")

    payload = {
        "script_version": SCRIPT_VERSION,
        "script_sha256": file_sha256(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "config": {
            "years": args.years,
            "ticks_per_year": TICKS_PER_YEAR,
            "n": n,
            "sigma": SIGMA,
            "amplitude": AMPLITUDE,
            "seeds": args.seeds,
            "calib_seeds": args.calib_seeds,
            "mdr_seeds": args.mdr_seeds,
            "horizon_seeds": args.horizon_seeds,
            "horizon_factors": list(HORIZON_FACTORS),
            "target_false_alarm": TARGET_FALSE_ALARM,
            "eprocess_rho": E_RHO,
        },
        "self_tests": self_tests,
        "calibration": calibration,
        "results": results,
        "finite_horizon_mdr50": mdr,
        "horizon_robustness": hz,
        "leaky_fixed_point_control": fixed,
        "leaky_effective_memory_control": eff,
        "legacy_predictions": [
            {"id": p[0], "kind": p[1], "statement": p[2],
             "historical_v1_1_verdict": LEGACY_HISTORICAL_VERDICTS[p[0]]}
            for p in LEGACY_PREDICTIONS
        ],
        "legacy_prediction_checks": legacy_checks,
        "post_pilot_targets": [
            {"id": p[0], "kind": p[1], "statement": p[2]} for p in POST_PILOT_TARGETS
        ],
        "post_pilot_target_checks": target_checks,
        "scope": {
            "research_not_canon": True,
            "tests_complete_thde": False,
            "tests_all_nexus_barriers": False,
            "ramp_mdr_is_asymptotic_proof": False,
            "raw_sqrt_is_anytime_valid": False,
            "eprocess_anytime_valid_under_modeled_gaussian_null": True,
            "known_epoch_bank_implements_reference_migration": False,
            "crosschannel_proves_truth": False,
        },
    }

    if args.json:
        Path(args.json).write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"JSON written to {args.json}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
