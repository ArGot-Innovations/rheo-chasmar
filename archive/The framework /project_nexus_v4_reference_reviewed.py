#!/usr/bin/env python3
"""
Project Nexus v4.0 — CA / TUCR / HTNLA / Maera reference demonstrator.

NumPy-only, deterministic, auditable implementation of:
  * 1024D vacuum-safe quinary HSL bit planes
  * HTNLA min-magnitude binding and explicit partial unbinding
  * exact admissible-set semantic reconstruction
  * discrete-to-continuous inverse bridge (E_err, RPE, Novelty)
  * bounded 11D Cyrae controller with RK4, resource law, and 666D friction
  * salience-driven deterministic k-WTA
  * TUCR integrate -> compete -> resonate -> transcend orchestration
  * hybrid jump events, fail-closed invariant guard, and qbin-like snapshots
  * Maera as a stateless constrained renderer only

The numerical controller gains are architecture calibration candidates. They are
versioned here so they cannot be silently changed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Optional, Sequence

import numpy as np


# =============================================================================
# 1. CANONICAL GEOMETRY AND CALIBRATION CANDIDATES
# =============================================================================
DIM = 1024
WORD_BITS = 64
WORDS = (DIM + WORD_BITS - 1) // WORD_BITS
K_WALL = 307                  # <=30% retained activation, >=70% structural vacuum
COUPLING_DIM = 666
EPS = 1e-12
E_MAX = 1.0
SCHEMA_VERSION = "project-nexus-v4.0"

STATE_LABELS = (
    "NE", "DA", "5HT", "ACh", "Glu", "GABA",
    "Perception", "Cognition", "Affect", "Volition", "Self",
)

LAMBDA = np.diag(
    [1.30, 1.25, 1.20, 1.25, 1.35, 1.35, 1.15, 1.10, 1.15, 1.10, 1.05]
).astype(np.float64)

W_C = np.array([
    [ 0.05, 0.00, -0.08, 0.08, 0.10, -0.12, 0.10, 0.06, 0.08, 0.06, 0.00],
    [ 0.06, 0.08, -0.12, 0.02, 0.05, -0.10, 0.00, 0.10, 0.18, 0.16, 0.08],
    [-0.04,-0.06,  0.10, 0.00,-0.08,  0.10,-0.02, 0.00,-0.06,-0.04, 0.12],
    [ 0.12, 0.00, -0.04, 0.08, 0.10, -0.08, 0.14, 0.12, 0.00, 0.04,-0.02],
    [ 0.06, 0.08, -0.10, 0.06, 0.10, -0.16, 0.12, 0.14, 0.08, 0.10, 0.00],
    [-0.02,-0.02,  0.10,-0.02, 0.12,  0.06, 0.00, 0.00, 0.05,-0.02, 0.04],
    [ 0.16, 0.02, -0.06, 0.18, 0.18, -0.12, 0.12, 0.12, 0.00, 0.00,-0.04],
    [ 0.10, 0.12,  0.00, 0.10, 0.14, -0.10, 0.18, 0.16, 0.05, 0.12, 0.08],
    [ 0.18, 0.10,  0.12, 0.00, 0.05, -0.18, 0.04, 0.04, 0.12, 0.12, 0.10],
    [ 0.08, 0.18, -0.04, 0.02, 0.12, -0.10, 0.00, 0.16, 0.16, 0.16, 0.08],
    [ 0.04, 0.08,  0.16, 0.00, 0.00, -0.10, 0.02, 0.08, 0.12, 0.14, 0.18],
], dtype=np.float64)

W_E = np.array([0.20, 0.05, 0.00, 0.20, 1.00, 0.25, 0.70, 0.45, 0.10, 0.10, -0.05])
W_R = np.array([0.20, 1.00,-0.15, 0.05, 0.25, 0.10, 0.00, 0.30, 0.55, 0.35,  0.10])
W_N = np.array([1.00, 0.20,-0.05, 0.95, 0.30, 0.05, 0.40, 0.25, 0.15, 0.10, -0.10])
BIAS = np.array([0.10, 0.08, 0.12, 0.10, 0.05, 0.10, 0.08, 0.10, 0.06, 0.06, 0.08])

# Inverse-bridge quinary mismatch weights.
ALPHA_OCC = 0.25
ALPHA_OCC_U2 = 0.125
BETA_SIGN = 0.50
GAMMA_MAG = 0.125
COST_MAX = max(ALPHA_OCC + ALPHA_OCC_U2, BETA_SIGN + GAMMA_MAG)

# Resource-law gains.
ALPHA_C = 0.25
ALPHA_R = 0.18
ALPHA_N = 0.14
RHO_CR = 0.08

# 11D -> k-WTA affine bridge.
K0 = 256.0
A_DA = 96.0
B_5HT = 64.0
C_GABA = 72.0
D_TEMP = 32.0

# 666D spectral friction.
GAMMA_M = 28.0
BETA_M = 2.4

# Salience-kernel candidate gains. Stabilizing channels subtract salience.
SALIENCE_DECAY = 0.60
SALIENCE_DA = 0.90
SALIENCE_ACH = 0.80
SALIENCE_GABA = 0.45
SALIENCE_5HT = 0.30

_ALLOWED_QUINARY = np.array([-2, -1, 0, 1, 2], dtype=np.int8)
_FULL_WORD_MASK = np.full(WORDS, np.uint64(0xFFFFFFFFFFFFFFFF), dtype=np.uint64)
if DIM % WORD_BITS:
    _FULL_WORD_MASK[-1] = np.uint64((1 << (DIM % WORD_BITS)) - 1)


# =============================================================================
# 2. LOW-LEVEL UTILITIES
# =============================================================================
def _popcount_words(words: np.ndarray) -> int:
    return sum(int(word).bit_count() for word in words)


def _pack_bits(bits: np.ndarray) -> np.ndarray:
    arr = np.asarray(bits, dtype=np.uint8)
    if arr.shape != (DIM,):
        raise ValueError(f"bit array must have shape ({DIM},), got {arr.shape}")
    packed = np.packbits(arr, bitorder="little")
    return np.frombuffer(packed.tobytes(), dtype="<u8").astype(np.uint64, copy=True)


def _unpack_bits(words: np.ndarray) -> np.ndarray:
    arr = np.asarray(words, dtype=np.uint64)
    if arr.shape != (WORDS,):
        raise ValueError(f"packed plane must have shape ({WORDS},), got {arr.shape}")
    little = arr.astype("<u8", copy=False)
    return np.unpackbits(little.view(np.uint8), bitorder="little")[:DIM].astype(bool)


def _stable_sigmoid(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64)
    out = np.empty_like(x)
    pos = x >= 0.0
    out[pos] = 1.0 / (1.0 + np.exp(-x[pos]))
    exp_x = np.exp(x[~pos])
    out[~pos] = exp_x / (1.0 + exp_x)
    return out


def _validate_scalar(value: float, name: str, lo: float, hi: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value < lo or value > hi:
        raise ValueError(f"{name} must be finite and in [{lo}, {hi}], got {value}")
    return value


def _quinary_cost_dense(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Per-coordinate normalized mismatch cost in [0, 1]."""
    a = np.asarray(a, dtype=np.int8)
    b = np.asarray(b, dtype=np.int8)
    aa = a != 0
    ab = b != 0
    ua = np.abs(a) == 2
    ub = np.abs(b) == 2
    sa = a < 0
    sb = b < 0
    occ = aa ^ ab
    overlap = aa & ab
    cost = (
        ALPHA_OCC * occ
        + ALPHA_OCC_U2 * (occ & (ua | ub))
        + BETA_SIGN * (overlap & (sa ^ sb))
        + GAMMA_MAG * (overlap & (ua ^ ub))
    )
    return cost.astype(np.float64) / COST_MAX


def _hash_arrays(arrays: dict[str, np.ndarray], metadata: dict) -> str:
    h = hashlib.sha256()
    for key in sorted(arrays):
        arr = np.ascontiguousarray(arrays[key])
        h.update(key.encode("utf-8"))
        h.update(str(arr.dtype).encode("ascii"))
        h.update(str(arr.shape).encode("ascii"))
        h.update(arr.tobytes())
    h.update(json.dumps(metadata, sort_keys=True, separators=(",", ":")).encode("utf-8"))
    return h.hexdigest()


def _calibration_fingerprint() -> str:
    """
    Hash of every numerical calibration constant this module ships with.

    Snapshots record this value so a restore can detect that the code's
    calibration gains have drifted from whatever produced the snapshot,
    instead of silently running old state through new dynamics.
    """
    h = hashlib.sha256()
    constants = {
        "LAMBDA": LAMBDA, "W_C": W_C, "W_E": W_E, "W_R": W_R, "W_N": W_N, "BIAS": BIAS,
        "ALPHA_OCC": ALPHA_OCC, "ALPHA_OCC_U2": ALPHA_OCC_U2, "BETA_SIGN": BETA_SIGN,
        "GAMMA_MAG": GAMMA_MAG, "ALPHA_C": ALPHA_C, "ALPHA_R": ALPHA_R, "ALPHA_N": ALPHA_N,
        "RHO_CR": RHO_CR, "K0": K0, "A_DA": A_DA, "B_5HT": B_5HT, "C_GABA": C_GABA,
        "D_TEMP": D_TEMP, "GAMMA_M": GAMMA_M, "BETA_M": BETA_M, "K_WALL": K_WALL,
        "SALIENCE_DECAY": SALIENCE_DECAY, "SALIENCE_DA": SALIENCE_DA,
        "SALIENCE_ACH": SALIENCE_ACH, "SALIENCE_GABA": SALIENCE_GABA, "SALIENCE_5HT": SALIENCE_5HT,
    }
    for key in sorted(constants):
        value = constants[key]
        h.update(key.encode("utf-8"))
        if isinstance(value, np.ndarray):
            h.update(np.ascontiguousarray(value, dtype=np.float64).tobytes())
        else:
            h.update(repr(float(value)).encode("ascii"))
    return h.hexdigest()


# =============================================================================
# 3. HSL QUINARY SUBSTRATE
# =============================================================================
@dataclass(frozen=True)
class KWTAReport:
    requested: int
    before: int
    after: int
    pruned: int
    cutoff_score: float


class QuinaryHypervector:
    """
    1024D quinary vector encoded in three uint64 planes.

    sign: 1 means negative, but only on active coordinates.
    mag1: active coordinates with |x| == 1.
    mag2: active coordinates with |x| == 2.

    Invariants:
      mag1 & mag2 == 0
      sign & ~(mag1 | mag2) == 0
    """

    __slots__ = ("sign", "mag1", "mag2")

    def __init__(
        self,
        sign: Optional[np.ndarray] = None,
        mag1: Optional[np.ndarray] = None,
        mag2: Optional[np.ndarray] = None,
        *,
        reject_overlap: bool = True,
    ) -> None:
        self.sign = np.zeros(WORDS, dtype=np.uint64) if sign is None else np.asarray(sign, dtype=np.uint64).copy()
        self.mag1 = np.zeros(WORDS, dtype=np.uint64) if mag1 is None else np.asarray(mag1, dtype=np.uint64).copy()
        self.mag2 = np.zeros(WORDS, dtype=np.uint64) if mag2 is None else np.asarray(mag2, dtype=np.uint64).copy()
        for name, plane in (("sign", self.sign), ("mag1", self.mag1), ("mag2", self.mag2)):
            if plane.shape != (WORDS,):
                raise ValueError(f"{name} must have shape ({WORDS},), got {plane.shape}")
        self._canonicalize(reject_overlap=reject_overlap)

    def _canonicalize(self, *, reject_overlap: bool) -> None:
        self.sign &= _FULL_WORD_MASK
        self.mag1 &= _FULL_WORD_MASK
        self.mag2 &= _FULL_WORD_MASK
        overlap = self.mag1 & self.mag2
        if np.any(overlap):
            if reject_overlap:
                raise ValueError("mag1 and mag2 overlap; quinary one-hot magnitude invariant violated")
            self.mag2 &= ~overlap
        # Load-bearing vacuum scrub: inactive coordinates can never retain sign.
        self.sign &= self.active

    @property
    def active(self) -> np.ndarray:
        return self.mag1 | self.mag2

    @property
    def popcount(self) -> int:
        return _popcount_words(self.active)

    @property
    def vacuum_fraction(self) -> float:
        return 1.0 - self.popcount / DIM

    def copy(self) -> "QuinaryHypervector":
        return QuinaryHypervector(self.sign, self.mag1, self.mag2)

    def validate(self) -> None:
        overlap = self.mag1 & self.mag2
        leaked_sign = self.sign & ~self.active & _FULL_WORD_MASK
        if np.any(overlap):
            raise AssertionError("P_M1 & P_M2 != 0")
        if np.any(leaked_sign):
            raise AssertionError("P_A=0 => P_S=0 violated")

    def fingerprint(self) -> str:
        h = hashlib.sha256()
        h.update(self.sign.astype("<u8", copy=False).tobytes())
        h.update(self.mag1.astype("<u8", copy=False).tobytes())
        h.update(self.mag2.astype("<u8", copy=False).tobytes())
        return h.hexdigest()

    @staticmethod
    def zero() -> "QuinaryHypervector":
        return QuinaryHypervector()

    @staticmethod
    def random(
        p_zero: float = 0.70,
        p_mag2_given_active: float = 0.15,
        *,
        seed: Optional[int] = None,
        rng: Optional[np.random.Generator] = None,
    ) -> "QuinaryHypervector":
        p_zero = _validate_scalar(p_zero, "p_zero", 0.0, 1.0)
        p_mag2_given_active = _validate_scalar(
            p_mag2_given_active, "p_mag2_given_active", 0.0, 1.0
        )
        if rng is None:
            rng = np.random.default_rng(seed)
        active = rng.random(DIM) >= p_zero
        mag2 = active & (rng.random(DIM) < p_mag2_given_active)
        mag1 = active & ~mag2
        sign = active & (rng.integers(0, 2, size=DIM, dtype=np.uint8).astype(bool))
        return QuinaryHypervector(_pack_bits(sign), _pack_bits(mag1), _pack_bits(mag2))

    @staticmethod
    def from_dense(values: np.ndarray) -> "QuinaryHypervector":
        arr = np.asarray(values)
        if arr.shape != (DIM,):
            raise ValueError(f"dense vector must have shape ({DIM},), got {arr.shape}")
        if not np.all(np.isfinite(arr)) or not np.all(arr == np.rint(arr)):
            raise ValueError("dense vector must contain finite integers")
        q = arr.astype(np.int8, copy=False)
        if not np.all(np.isin(q, _ALLOWED_QUINARY)):
            raise ValueError("dense vector contains values outside {-2,-1,0,1,2}")
        active = q != 0
        sign = q < 0
        mag2 = np.abs(q) == 2
        mag1 = active & ~mag2
        return QuinaryHypervector(_pack_bits(sign), _pack_bits(mag1), _pack_bits(mag2))

    def to_dense(self) -> np.ndarray:
        active = _unpack_bits(self.active)
        sign = _unpack_bits(self.sign)
        mag2 = _unpack_bits(self.mag2)
        magnitude = active.astype(np.int8) + mag2.astype(np.int8)
        values = magnitude.copy()
        values[sign & active] *= -1
        return values

    def apply_k_wta(self, k_allow: int, salience: Optional[np.ndarray] = None) -> KWTAReport:
        """
        Deterministic salience-preserving k-WTA.

        Random pruning is intentionally forbidden: equal inputs and equal salience must
        produce an identical survivor set. Magnitude 2 receives a small tie-breaking prior,
        followed by coordinate index for total determinism.
        """
        if not isinstance(k_allow, (int, np.integer)):
            raise TypeError("k_allow must be an integer")
        k_allow = int(np.clip(k_allow, 0, DIM))
        active_idx = np.flatnonzero(_unpack_bits(self.active))
        before = int(active_idx.size)
        if before <= k_allow:
            return KWTAReport(k_allow, before, before, 0, float("-inf"))

        if salience is None:
            scores = np.zeros(DIM, dtype=np.float64)
        else:
            scores = np.asarray(salience, dtype=np.float64)
            if scores.shape != (DIM,) or not np.all(np.isfinite(scores)):
                raise ValueError(f"salience must be finite with shape ({DIM},)")

        mag2 = _unpack_bits(self.mag2)
        active_scores = scores[active_idx] + 0.05 * mag2[active_idx].astype(np.float64)
        order = np.lexsort((active_idx, -active_scores))
        prune_idx = active_idx[order[k_allow:]]
        cutoff = float(active_scores[order[k_allow - 1]]) if k_allow > 0 else float("inf")

        for idx in prune_idx:
            word = int(idx) // WORD_BITS
            bit = int(idx) % WORD_BITS
            keep_mask = np.uint64(~(np.uint64(1) << np.uint64(bit)))
            self.sign[word] &= keep_mask
            self.mag1[word] &= keep_mask
            self.mag2[word] &= keep_mask

        self._canonicalize(reject_overlap=True)
        return KWTAReport(k_allow, before, self.popcount, before - self.popcount, cutoff)

    def bind(self, other: "QuinaryHypervector") -> "QuinaryHypervector":
        """HTNLA conservative binding: XOR sign and min magnitude."""
        c_mag2 = self.mag2 & other.mag2
        c_mag1 = (
            (self.mag1 & other.mag1)
            | (self.mag1 & other.mag2)
            | (self.mag2 & other.mag1)
        )
        c_active = c_mag1 | c_mag2
        c_sign = (self.sign ^ other.sign) & c_active
        return QuinaryHypervector(c_sign, c_mag1, c_mag2)

    @staticmethod
    def bundle(
        vectors: Sequence["QuinaryHypervector"],
        weights: Optional[Sequence[float]] = None,
        activation_threshold: float = 0.25,
    ) -> "QuinaryHypervector":
        """Clipped weighted-majority bundling; binding remains magnitude-contractive."""
        if not vectors:
            return QuinaryHypervector.zero()
        dense = np.stack([v.to_dense().astype(np.float64) for v in vectors], axis=0)
        if weights is None:
            w = np.ones(len(vectors), dtype=np.float64)
        else:
            w = np.asarray(weights, dtype=np.float64)
            if w.shape != (len(vectors),) or not np.all(np.isfinite(w)) or np.allclose(w, 0.0):
                raise ValueError("weights must be finite, nonzero, and match vectors")
        score = np.average(dense, axis=0, weights=np.abs(w))
        out = np.zeros(DIM, dtype=np.int8)
        active = np.abs(score) >= activation_threshold
        out[active] = np.where(score[active] < 0.0, -1, 1)
        strong = np.abs(score) >= 1.5
        out[strong] *= 2
        return QuinaryHypervector.from_dense(out)

    def inverse(self) -> "QuinaryHypervector":
        return QuinaryHypervector((~self.sign) & self.active, self.mag1, self.mag2)

    def permute(self, offset: int) -> "QuinaryHypervector":
        return QuinaryHypervector.from_dense(np.roll(self.to_dense(), int(offset)))

    def dot(self, other: "QuinaryHypervector") -> float:
        overlap = self.active & other.active
        sign_clash = (self.sign ^ other.sign) & overlap
        sign_match = (~(self.sign ^ other.sign)) & overlap
        m11 = self.mag1 & other.mag1
        m12 = (self.mag1 & other.mag2) | (self.mag2 & other.mag1)
        m22 = self.mag2 & other.mag2

        def weighted(mask: np.ndarray) -> float:
            return float(
                _popcount_words(mask & m11)
                + 2 * _popcount_words(mask & m12)
                + 4 * _popcount_words(mask & m22)
            )

        return weighted(sign_match) - weighted(sign_clash)

    def norm(self) -> float:
        return float(math.sqrt(_popcount_words(self.mag1) + 4 * _popcount_words(self.mag2)))

    def cosine_similarity(self, other: "QuinaryHypervector") -> float:
        denom = self.norm() * other.norm()
        return 0.0 if denom <= EPS else float(np.clip(self.dot(other) / denom, -1.0, 1.0))

    def partial_unbind(self, binder: "QuinaryHypervector") -> "PartialUnbindResult":
        a_b = binder.active
        a_c = self.active

        impossible = (a_c & ~a_b & _FULL_WORD_MASK) | (self.mag2 & ~binder.mag2 & _FULL_WORD_MASK)
        sign_known = a_b & a_c
        sign_hat = (self.sign ^ binder.sign) & sign_known

        known_zero = a_b & ~a_c & _FULL_WORD_MASK
        exact_mag1 = binder.mag2 & a_c & ~self.mag2 & _FULL_WORD_MASK
        exact_mag2 = binder.mag2 & self.mag2
        ambiguous = a_b & ~binder.mag2 & a_c & _FULL_WORD_MASK
        unknown = ~a_b & _FULL_WORD_MASK

        return PartialUnbindResult(
            sign_hat=sign_hat,
            known_zero=known_zero,
            exact_mag1=exact_mag1,
            exact_mag2=exact_mag2,
            ambiguous=ambiguous,
            unknown=unknown,
            impossible=impossible,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, QuinaryHypervector):
            return False
        return (
            np.array_equal(self.sign, other.sign)
            and np.array_equal(self.mag1, other.mag1)
            and np.array_equal(self.mag2, other.mag2)
        )


@dataclass(frozen=True)
class PartialUnbindResult:
    sign_hat: np.ndarray
    known_zero: np.ndarray
    exact_mag1: np.ndarray
    exact_mag2: np.ndarray
    ambiguous: np.ndarray
    unknown: np.ndarray
    impossible: np.ndarray

    @property
    def informative_mask(self) -> np.ndarray:
        return self.known_zero | self.exact_mag1 | self.exact_mag2 | self.ambiguous

    @property
    def informative_count(self) -> int:
        return _popcount_words(self.informative_mask)

    @property
    def exact_count(self) -> int:
        return _popcount_words(self.known_zero | self.exact_mag1 | self.exact_mag2)

    @property
    def ambiguous_count(self) -> int:
        return _popcount_words(self.ambiguous)

    @property
    def unknown_count(self) -> int:
        return _popcount_words(self.unknown)

    @property
    def impossible_count(self) -> int:
        return _popcount_words(self.impossible)

    def distance(self, candidate: QuinaryHypervector) -> float:
        """Exact masked admissible-set distance; erased dimensions contribute nothing."""
        if self.impossible_count:
            return 1.0
        q = candidate.to_dense()
        sign = _unpack_bits(self.sign_hat)
        known_zero = _unpack_bits(self.known_zero)
        exact1 = _unpack_bits(self.exact_mag1)
        exact2 = _unpack_bits(self.exact_mag2)
        ambiguous = _unpack_bits(self.ambiguous)
        informative = known_zero | exact1 | exact2 | ambiguous
        n = int(np.count_nonzero(informative))
        if n == 0:
            return 0.0

        cost = np.zeros(DIM, dtype=np.float64)
        if np.any(known_zero):
            cost[known_zero] = _quinary_cost_dense(q[known_zero], np.zeros(np.count_nonzero(known_zero), dtype=np.int8))
        if np.any(exact1):
            target = np.where(sign[exact1], -1, 1).astype(np.int8)
            cost[exact1] = _quinary_cost_dense(q[exact1], target)
        if np.any(exact2):
            target = np.where(sign[exact2], -2, 2).astype(np.int8)
            cost[exact2] = _quinary_cost_dense(q[exact2], target)
        if np.any(ambiguous):
            target1 = np.where(sign[ambiguous], -1, 1).astype(np.int8)
            target2 = np.where(sign[ambiguous], -2, 2).astype(np.int8)
            c1 = _quinary_cost_dense(q[ambiguous], target1)
            c2 = _quinary_cost_dense(q[ambiguous], target2)
            cost[ambiguous] = np.minimum(c1, c2)
        return float(np.clip(np.sum(cost[informative]) / n, 0.0, 1.0))


# =============================================================================
# 4. WARM MEMORY AND EXACT SEMANTIC SNAP
# =============================================================================
@dataclass
class MemoryRecord:
    name: str
    vector: QuinaryHypervector
    protected: bool = False
    hits: int = 0


@dataclass(frozen=True)
class SnapResult:
    name: Optional[str]
    vector: Optional[QuinaryHypervector]
    distance: float
    confidence: float
    margin: float
    evidence_coverage: float
    accepted: bool
    reason: str


class WarmMemory:
    def __init__(self) -> None:
        self.records: list[MemoryRecord] = []

    def __len__(self) -> int:
        return len(self.records)

    def add(self, name: str, vector: QuinaryHypervector, *, protected: bool = False) -> None:
        if any(record.name == name for record in self.records):
            raise ValueError(f"duplicate memory name: {name}")
        vector.validate()
        self.records.append(MemoryRecord(name=name, vector=vector.copy(), protected=protected))

    def add_random(self, count: int, *, seed: int, p_zero: float = 0.62) -> None:
        rng = np.random.default_rng(seed)
        for i in range(int(count)):
            self.add(f"distractor_{i:04d}", QuinaryHypervector.random(p_zero=p_zero, rng=rng))

    def dense_matrix(self) -> np.ndarray:
        if not self.records:
            return np.empty((0, DIM), dtype=np.int8)
        return np.stack([record.vector.to_dense() for record in self.records], axis=0)

    def vectors(self) -> list[QuinaryHypervector]:
        return [record.vector for record in self.records]

    def semantic_snap(
        self,
        partial: PartialUnbindResult,
        *,
        max_distance: float = 0.24,
        min_margin: float = 0.01,
        min_informative: int = 24,
    ) -> SnapResult:
        if partial.impossible_count:
            return SnapResult(None, None, 1.0, 0.0, 0.0, 0.0, False, "impossible composite")
        if not self.records:
            return SnapResult(None, None, 1.0, 0.0, 0.0, 0.0, False, "empty warm memory")

        coverage = partial.informative_count / DIM
        if partial.informative_count < min_informative:
            return SnapResult(None, None, 1.0, 0.0, 0.0, coverage, False, "insufficient evidence")

        distances = np.array([partial.distance(record.vector) for record in self.records], dtype=np.float64)
        order = np.argsort(distances, kind="stable")
        best_idx = int(order[0])
        best = float(distances[best_idx])
        second = float(distances[order[1]]) if len(order) > 1 else 1.0
        margin = max(0.0, second - best)
        confidence = float(np.clip((1.0 - best) * (0.5 + 0.5 * coverage), 0.0, 1.0))
        accepted = best <= max_distance and margin >= min_margin
        reason = "accepted" if accepted else ("distance threshold" if best > max_distance else "ambiguous margin")
        record = self.records[best_idx]
        if accepted:
            record.hits += 1
        return SnapResult(
            name=record.name,
            vector=record.vector.copy() if accepted else None,
            distance=best,
            confidence=confidence,
            margin=margin,
            evidence_coverage=coverage,
            accepted=accepted,
            reason=reason,
        )


# =============================================================================
# 5. DISCRETE -> CONTINUOUS INVERSE BRIDGE
# =============================================================================
@dataclass(frozen=True)
class BridgeSignals:
    prediction_error: float
    rpe: float
    novelty: float
    value_expected: float
    value_actual: float
    density_deficit: float
    manifold_residual: float
    coordinate_error: np.ndarray = field(repr=False)
    coordinate_rpe: np.ndarray = field(repr=False)
    coordinate_novelty: np.ndarray = field(repr=False)


class InverseBridge:
    def __init__(self, *, k_neighbors: int = 8, subspace_rank: int = 4, manifold_weight: float = 0.5):
        if k_neighbors < 1:
            raise ValueError("k_neighbors must be >= 1")
        if subspace_rank < 0:
            raise ValueError("subspace_rank must be >= 0")
        self.k_neighbors = int(k_neighbors)
        self.subspace_rank = int(subspace_rank)
        self.manifold_weight = _validate_scalar(manifold_weight, "manifold_weight", 0.0, 1.0)

    @staticmethod
    def prediction_error(expected: QuinaryHypervector, actual: QuinaryHypervector) -> float:
        a_e, a_a = expected.active, actual.active
        u_e, u_a = expected.mag2, actual.mag2
        support_union = a_e | a_a
        n_union = max(1, _popcount_words(support_union))
        occ = a_e ^ a_a
        overlap = a_e & a_a
        numerator = (
            ALPHA_OCC * _popcount_words(occ)
            + ALPHA_OCC_U2 * _popcount_words(occ & (u_e | u_a))
            + BETA_SIGN * _popcount_words(overlap & (expected.sign ^ actual.sign))
            + GAMMA_MAG * _popcount_words(overlap & (u_e ^ u_a))
        )
        return float(np.clip(numerator / (COST_MAX * n_union), 0.0, 1.0))

    @staticmethod
    def value_projection(state: QuinaryHypervector, anchor: QuinaryHypervector) -> float:
        q_anchor = anchor.to_dense().astype(np.float64)
        denom = 2.0 * float(np.sum(np.abs(q_anchor)))
        if denom <= EPS:
            return 0.0
        return float(np.clip(np.dot(state.to_dense().astype(np.float64), q_anchor) / denom, -1.0, 1.0))

    def compute(
        self,
        expected: QuinaryHypervector,
        actual: QuinaryHypervector,
        value_anchor: QuinaryHypervector,
        warm_memory: WarmMemory,
    ) -> BridgeSignals:
        q_e = expected.to_dense()
        q_a = actual.to_dense()
        q_v = value_anchor.to_dense().astype(np.float64)

        coord_error = _quinary_cost_dense(q_e, q_a)
        e_err = self.prediction_error(expected, actual)
        v_e = self.value_projection(expected, value_anchor)
        v_a = self.value_projection(actual, value_anchor)
        rpe = float(np.clip((v_a - v_e) / 2.0, -1.0, 1.0))

        anchor_l1 = float(np.sum(np.abs(q_v)))
        if anchor_l1 <= EPS:
            coord_rpe = np.zeros(DIM, dtype=np.float64)
        else:
            coord_rpe = ((q_a.astype(np.float64) - q_e.astype(np.float64)) * q_v) / (4.0 * anchor_l1)

        memories = warm_memory.vectors()
        if not memories:
            memories = [expected]
        distances = np.array([self.prediction_error(mem, actual) for mem in memories], dtype=np.float64)
        k = min(self.k_neighbors, len(memories))
        nearest_idx = np.argsort(distances, kind="stable")[:k]
        rho = float(np.mean(distances[nearest_idx]))
        neighbor_dense = np.stack([memories[int(i)].to_dense() for i in nearest_idx], axis=0).astype(np.float64)
        coord_novelty = np.mean(
            np.stack([_quinary_cost_dense(row.astype(np.int8), q_a) for row in neighbor_dense], axis=0),
            axis=0,
        )

        eta = rho
        if k >= 3 and self.subspace_rank > 0:
            mean = np.mean(neighbor_dense, axis=0)
            centered = neighbor_dense - mean
            delta = q_a.astype(np.float64) - mean
            denom = float(np.dot(delta, delta))
            if denom > EPS:
                _, _, vt = np.linalg.svd(centered, full_matrices=False)
                rank = min(self.subspace_rank, k - 1, vt.shape[0])
                if rank > 0:
                    basis = vt[:rank]
                    projection = basis.T @ (basis @ delta)
                    residual = delta - projection
                    eta = float(np.clip(np.dot(residual, residual) / denom, 0.0, 1.0))

        novelty = float(np.clip(self.manifold_weight * eta + (1.0 - self.manifold_weight) * rho, 0.0, 1.0))
        return BridgeSignals(
            prediction_error=e_err,
            rpe=rpe,
            novelty=novelty,
            value_expected=v_e,
            value_actual=v_a,
            density_deficit=rho,
            manifold_residual=eta,
            coordinate_error=coord_error,
            coordinate_rpe=coord_rpe,
            coordinate_novelty=coord_novelty,
        )


# =============================================================================
# 6. 666D COUPLING GEOMETRY AND CONTINUOUS CYRAE CONTROLLER
# =============================================================================
class SymmetricCouplingGeometry:
    """
    Actual 666D symmetric operator stored as diagonal + low-rank factors.

    Symmetry is deliberate in this demonstrator: spectral abscissa and logarithmic
    norm are the same largest eigenvalue, so the stability score can be estimated by
    deterministic shifted power iteration without pretending a mock scalar is a matrix.
    """

    def __init__(self, *, dim: int = COUPLING_DIM, rank: int = 12, seed: int = 2026):
        if dim != COUPLING_DIM:
            raise ValueError(f"canonical coupling dimension is {COUPLING_DIM}")
        rng = np.random.default_rng(seed)
        self.dim = dim
        self.rank = int(rank)
        self.diagonal = rng.uniform(-0.36, -0.24, size=dim).astype(np.float64)
        raw = rng.normal(size=(dim, rank))
        self.basis, _ = np.linalg.qr(raw, mode="reduced")
        self.strengths = rng.uniform(0.05, 0.18, size=rank).astype(np.float64)
        self.base_alpha, self.residual = self._largest_eigenvalue()

    def matvec(self, x: np.ndarray) -> np.ndarray:
        x = np.asarray(x, dtype=np.float64)
        return self.diagonal * x + self.basis @ (self.strengths * (self.basis.T @ x))

    def _largest_eigenvalue(self, max_iter: int = 160, tol: float = 1e-11) -> tuple[float, float]:
        # Shift makes all eigenvalues positive, allowing ordinary power iteration to
        # select the largest algebraic eigenvalue rather than the largest magnitude.
        shift = 1.0
        x = np.ones(self.dim, dtype=np.float64)
        x /= np.linalg.norm(x)
        previous = -np.inf
        for _ in range(max_iter):
            y = self.matvec(x) + shift * x
            norm = np.linalg.norm(y)
            if norm <= EPS:
                return 0.0, 0.0
            x = y / norm
            rayleigh = float(np.dot(x, self.matvec(x)))
            if abs(rayleigh - previous) <= tol:
                break
            previous = rayleigh
        residual = float(np.linalg.norm(self.matvec(x) - rayleigh * x))
        return rayleigh, residual

    def effective_alpha(self, resonance_shift: float = 0.0) -> float:
        # Adding shift*I moves every eigenvalue by exactly the same amount.
        return float(self.base_alpha + resonance_shift)


@dataclass(frozen=True)
class HybridEvent:
    name: str
    severity: float
    spectral_shift: float = 0.90
    resource_drain: float = 0.35
    freeze: bool = True

    def __post_init__(self) -> None:
        _validate_scalar(self.severity, "severity", 0.0, 1.0)
        if self.spectral_shift < 0.0 or self.resource_drain < 0.0:
            raise ValueError("event gains must be nonnegative")


@dataclass(frozen=True)
class ControllerOutput:
    state: np.ndarray
    cognitive_resource: float
    energy_budget: float
    k_allow: int
    k_affine: float
    spectral_alpha: float
    spectral_penalty: float
    norm_dcdt: float
    power_demand: float
    fail_safe_triggered: bool
    frozen: bool
    event_name: Optional[str]


class CyraeController:
    def __init__(self, coupling: SymmetricCouplingGeometry):
        self.coupling = coupling
        self.C = np.array([0.2, 0.5, 0.5, 0.3, 0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.8], dtype=np.float64)
        self.C_r = 0.5
        self.B = 0.85 * E_MAX
        self.dCdt = np.zeros(11, dtype=np.float64)
        self.freeze_cycles = 0

    def _dynamics(self, state: np.ndarray, signals: BridgeSignals) -> np.ndarray:
        drive = (
            W_C @ state
            + W_E * signals.prediction_error
            + W_R * signals.rpe
            + W_N * signals.novelty
            + BIAS
        )
        return -(LAMBDA @ state) + _stable_sigmoid(drive)

    def _apply_jump(self, event: HybridEvent) -> float:
        s = event.severity
        jump = np.zeros(11, dtype=np.float64)
        jump[0] = 0.30 * s       # NE
        jump[4] = 0.22 * s       # Glu
        jump[5] = 0.08 * s       # GABA counter-response
        jump[8] = 0.30 * s       # Affect
        jump[9] = -0.12 * s      # Volition temporarily constrained
        # Self is deliberately not directly rewritten by the event.
        self.C = np.clip(self.C + jump, 0.0, 1.0)
        self.B *= math.exp(-event.resource_drain * s)
        self.C_r = float(np.clip(self.C_r * (1.0 - 0.45 * s), 0.05, 1.0))
        if event.freeze:
            self.freeze_cycles = max(self.freeze_cycles, 2)
        return event.spectral_shift * s

    def step(self, signals: BridgeSignals, *, dt: float = 0.02, event: Optional[HybridEvent] = None) -> ControllerOutput:
        if not 0.0 < dt <= 0.25:
            raise ValueError("dt must be in (0, 0.25]")
        for value, name, lo, hi in (
            (signals.prediction_error, "prediction_error", 0.0, 1.0),
            (signals.rpe, "rpe", -1.0, 1.0),
            (signals.novelty, "novelty", 0.0, 1.0),
        ):
            _validate_scalar(value, name, lo, hi)

        event_shift = self._apply_jump(event) if event is not None else 0.0

        k1 = self._dynamics(self.C, signals)
        k2 = self._dynamics(np.clip(self.C + 0.5 * dt * k1, 0.0, 1.0), signals)
        k3 = self._dynamics(np.clip(self.C + 0.5 * dt * k2, 0.0, 1.0), signals)
        k4 = self._dynamics(np.clip(self.C + dt * k3, 0.0, 1.0), signals)
        self.dCdt = (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        self.C = np.clip(self.C + dt * self.dCdt, 0.0, 1.0)

        demand = float(
            ALPHA_C * np.dot(self.dCdt, self.dCdt)
            + ALPHA_R * signals.rpe ** 2
            + ALPHA_N * signals.novelty ** 2
        )
        self.B = float(np.clip(self.B + dt * (-(demand / (0.85 * E_MAX)) * self.B), 0.0, 0.85 * E_MAX))
        ceiling = 0.05 + 0.95 * (self.B / (0.85 * E_MAX))
        dcrdt = RHO_CR * (ceiling - self.C_r) - demand * (self.C_r - 0.05)
        self.C_r = float(np.clip(self.C_r + dt * dcrdt, 0.05, 1.0))

        # Explicit engineering closure: bounded bridge signals shift the 666D operator;
        # hybrid events add a separate jump contribution.
        resonance_shift = (
            0.18 * signals.prediction_error
            + 0.25 * signals.novelty
            + 0.18 * max(-signals.rpe, 0.0)
            + event_shift
        )
        alpha_hat = self.coupling.effective_alpha(resonance_shift)
        positive_alpha = max(0.0, alpha_hat)
        penalty = float(GAMMA_M * np.expm1(min(BETA_M * positive_alpha, 20.0)))

        da, ht5, gaba = self.C[1], self.C[2], self.C[5]
        temp = 1.0 - self.C[8]
        k_affine = K0 + A_DA * da - B_5HT * ht5 - C_GABA * gaba - D_TEMP * temp
        k_allow = int(np.clip(math.floor(k_affine - penalty), 1, K_WALL))

        norm_dcdt = float(np.linalg.norm(self.dCdt))
        dynamic_fail = norm_dcdt > 5.0 * self.C_r
        frozen = self.freeze_cycles > 0
        fail_safe = dynamic_fail or frozen
        if fail_safe:
            k_allow = max(1, k_allow // 2)
            # Receptor reset / safe-manifold projection.
            self.C[4] *= 0.85
            self.C[5] = min(1.0, self.C[5] + 0.08)
        if self.freeze_cycles > 0:
            self.freeze_cycles -= 1

        return ControllerOutput(
            state=self.C.copy(),
            cognitive_resource=self.C_r,
            energy_budget=self.B,
            k_allow=k_allow,
            k_affine=float(k_affine),
            spectral_alpha=float(alpha_hat),
            spectral_penalty=penalty,
            norm_dcdt=norm_dcdt,
            power_demand=demand,
            fail_safe_triggered=fail_safe,
            frozen=frozen,
            event_name=event.name if event else None,
        )


# =============================================================================
# 7. SALIENCE KERNEL, INVARIANT GEOMETRY, TUCR ORCHESTRATOR
# =============================================================================
class SalienceKernel:
    def __init__(self) -> None:
        self.weights = np.zeros(DIM, dtype=np.float64)
        self.previous_error = np.zeros(DIM, dtype=np.float64)

    def update(self, bridge: BridgeSignals, controller: ControllerOutput, *, dt: float, frozen: bool) -> np.ndarray:
        da = controller.state[1]
        ht5 = controller.state[2]
        ach = controller.state[3]
        gaba = controller.state[5]
        volatility = np.abs(bridge.coordinate_error - self.previous_error)
        derivative = (
            -SALIENCE_DECAY * self.weights
            + SALIENCE_DA * da * np.abs(bridge.coordinate_rpe)
            + SALIENCE_ACH * ach * bridge.coordinate_novelty
            - SALIENCE_GABA * gaba * bridge.coordinate_error
            - SALIENCE_5HT * ht5 * volatility
        )
        self.weights = np.clip(self.weights + dt * derivative, 0.0, 1.0)
        if frozen:
            self.weights *= 0.5
        self.previous_error = bridge.coordinate_error.copy()
        return self.weights.copy()

    def scores(self, vector: QuinaryHypervector, bridge: BridgeSignals) -> np.ndarray:
        magnitude_prior = 0.05 * np.abs(vector.to_dense()).astype(np.float64)
        # Preserve high-information mismatches long enough for adjudication.
        return self.weights + magnitude_prior + 0.20 * bridge.coordinate_error + 0.10 * bridge.coordinate_novelty


@dataclass(frozen=True)
class GuardReport:
    passed: bool
    violations: tuple[str, ...]


class InvariantGuard:
    def __init__(self, immutable_anchor: QuinaryHypervector):
        self.anchor_fingerprint = immutable_anchor.fingerprint()

    def audit(
        self,
        *,
        vector: QuinaryHypervector,
        anchor: QuinaryHypervector,
        controller: ControllerOutput,
        partial: PartialUnbindResult,
    ) -> GuardReport:
        violations: list[str] = []
        try:
            vector.validate()
        except AssertionError as exc:
            violations.append(str(exc))
        if anchor.fingerprint() != self.anchor_fingerprint:
            violations.append("immutable Value Anchor changed")
        if not np.all(np.isfinite(controller.state)) or not np.all((controller.state >= 0.0) & (controller.state <= 1.0)):
            violations.append("11D state left invariant cube")
        if not 0.05 <= controller.cognitive_resource <= 1.0:
            violations.append("cognitive resource left invariant interval")
        if not 0.0 <= controller.energy_budget <= 0.85 * E_MAX:
            violations.append("energy budget left admissible interval")
        if partial.impossible_count:
            violations.append(f"partial unbind contains {partial.impossible_count} impossible coordinates")
        return GuardReport(passed=not violations, violations=tuple(violations))


@dataclass(frozen=True)
class CycleResult:
    bridge: BridgeSignals
    controller: ControllerOutput
    kwta: KWTAReport
    partial: PartialUnbindResult
    snap: SnapResult
    guard: GuardReport
    gated_composite: QuinaryHypervector
    stage_trace: tuple[str, ...]


class MaeraActuator:
    """No memory, no controller, and no VSA operations: only constrained rendering."""

    @staticmethod
    def render(result: CycleResult) -> str:
        if not result.guard.passed:
            mode = "FAIL_CLOSED"
            action = "ABSTAIN"
        elif result.controller.fail_safe_triggered:
            mode = "SAFE_MODE"
            action = "RENDER" if result.snap.accepted else "ABSTAIN"
        else:
            mode = "NOMINAL"
            action = "RENDER" if result.snap.accepted else "ABSTAIN"

        memory = result.snap.name if result.snap.accepted else "NONE"
        return (
            f"[MAERA] action={action} mode={mode} memory={memory} "
            f"k={result.controller.k_allow}/{DIM} active={result.gated_composite.popcount} "
            f"snap_conf={result.snap.confidence:.3f} distance={result.snap.distance:.3f} "
            f"margin={result.snap.margin:.3f} E={result.bridge.prediction_error:.3f} "
            f"RPE={result.bridge.rpe:+.3f} N={result.bridge.novelty:.3f} "
            f"Cr={result.controller.cognitive_resource:.3f} guard={result.guard.passed}"
        )


class NexusRuntime:
    def __init__(self, *, seed: int = 2026, value_anchor: Optional[QuinaryHypervector] = None):
        self.seed = int(seed)
        self.coupling = SymmetricCouplingGeometry(seed=seed)
        self.controller = CyraeController(self.coupling)
        self.inverse_bridge = InverseBridge()
        self.salience = SalienceKernel()
        self.memory = WarmMemory()
        self.value_anchor = value_anchor.copy() if value_anchor is not None else QuinaryHypervector.random(p_zero=0.68, seed=seed + 1)
        self.guard = InvariantGuard(self.value_anchor)
        self.maera = MaeraActuator()

    def cycle(
        self,
        *,
        expected_constituent: QuinaryHypervector,
        binder: QuinaryHypervector,
        observed_composite: Optional[QuinaryHypervector] = None,
        dt: float = 0.02,
        event: Optional[HybridEvent] = None,
    ) -> CycleResult:
        stage: list[str] = []

        expected_composite = expected_constituent.bind(binder)
        observed = observed_composite.copy() if observed_composite is not None else expected_composite.copy()

        # TUCR / INTEGRATE: substrate evidence -> bounded continuous drives.
        bridge = self.inverse_bridge.compute(expected_composite, observed, self.value_anchor, self.memory)
        controller = self.controller.step(bridge, dt=dt, event=event)
        self.salience.update(bridge, controller, dt=dt, frozen=controller.frozen)
        stage.append("integrate")

        # TUCR / COMPETE: deterministic salience-driven sparsification.
        gated = observed.copy()
        scores = self.salience.scores(gated, bridge)
        kwta = gated.apply_k_wta(controller.k_allow, scores)
        stage.append("compete")

        # TUCR / RESONATE: exact partial inverse then topology-aware cleanup.
        partial = gated.partial_unbind(binder)
        snap = self.memory.semantic_snap(partial)
        stage.append("resonate")

        # HIGC-style fail-closed adjudication before outward rendering.
        guard = self.guard.audit(vector=gated, anchor=self.value_anchor, controller=controller, partial=partial)
        if not guard.passed and snap.accepted:
            snap = SnapResult(None, None, 1.0, 0.0, 0.0, 0.0, False, "invariant guard rejected cycle")

        # TUCR / TRANSCEND: emit a finite packet; no automatic identity mutation.
        stage.append("transcend")
        return CycleResult(
            bridge=bridge,
            controller=controller,
            kwta=kwta,
            partial=partial,
            snap=snap,
            guard=guard,
            gated_composite=gated,
            stage_trace=tuple(stage),
        )

    def save_snapshot(self, path: str | Path) -> Path:
        path = Path(path)
        memory_count = len(self.memory.records)
        sign = np.stack([r.vector.sign for r in self.memory.records], axis=0) if memory_count else np.empty((0, WORDS), dtype=np.uint64)
        mag1 = np.stack([r.vector.mag1 for r in self.memory.records], axis=0) if memory_count else np.empty((0, WORDS), dtype=np.uint64)
        mag2 = np.stack([r.vector.mag2 for r in self.memory.records], axis=0) if memory_count else np.empty((0, WORDS), dtype=np.uint64)
        arrays = {
            "controller_C": self.controller.C,
            "controller_dCdt": self.controller.dCdt,
            "controller_scalars": np.array([self.controller.C_r, self.controller.B, self.controller.freeze_cycles], dtype=np.float64),
            "salience_weights": self.salience.weights,
            "salience_previous_error": self.salience.previous_error,
            "anchor_sign": self.value_anchor.sign,
            "anchor_mag1": self.value_anchor.mag1,
            "anchor_mag2": self.value_anchor.mag2,
            "coupling_diagonal": self.coupling.diagonal,
            "coupling_basis": self.coupling.basis,
            "coupling_strengths": self.coupling.strengths,
            "memory_sign": sign,
            "memory_mag1": mag1,
            "memory_mag2": mag2,
        }
        metadata = {
            "schema": SCHEMA_VERSION,
            "dim": DIM,
            "coupling_dim": COUPLING_DIM,
            "seed": self.seed,
            "calibration_fingerprint": _calibration_fingerprint(),
            "memory": [
                {"name": r.name, "protected": r.protected, "hits": r.hits}
                for r in self.memory.records
            ],
        }
        digest = _hash_arrays(arrays, metadata)
        manifest = dict(metadata)
        manifest["sha256"] = digest
        arrays["manifest"] = np.frombuffer(
            json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode("utf-8"),
            dtype=np.uint8,
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("wb") as fh:
            np.savez_compressed(fh, **arrays)
        return path

    def restore_snapshot(self, path: str | Path, *, require_calibration_match: bool = True) -> None:
        with np.load(Path(path), allow_pickle=False) as data:
            manifest = json.loads(bytes(data["manifest"].tolist()).decode("utf-8"))
            if manifest.get("schema") != SCHEMA_VERSION or manifest.get("dim") != DIM:
                raise ValueError("snapshot schema or dimension mismatch")
            arrays = {key: data[key].copy() for key in data.files if key != "manifest"}
        expected_digest = manifest.pop("sha256")
        if _hash_arrays(arrays, manifest) != expected_digest:
            raise ValueError("snapshot checksum mismatch")

        record_count = len(manifest.get("memory", []))
        for key in ("memory_sign", "memory_mag1", "memory_mag2"):
            if arrays[key].shape[0] != record_count:
                raise ValueError(
                    f"snapshot manifest lists {record_count} memory records but {key} "
                    f"has {arrays[key].shape[0]} rows"
                )

        saved_fingerprint = manifest.get("calibration_fingerprint")
        current_fingerprint = _calibration_fingerprint()
        if saved_fingerprint != current_fingerprint:
            message = (
                "snapshot calibration fingerprint does not match this code's constants "
                "(the snapshot was produced by a different calibration of the gains); "
                "restoring anyway would run old state through different dynamics"
            )
            if require_calibration_match:
                raise ValueError(message)
            import warnings
            warnings.warn(message)

        self.controller.C = arrays["controller_C"].astype(np.float64)
        self.controller.dCdt = arrays["controller_dCdt"].astype(np.float64)
        scalars = arrays["controller_scalars"]
        self.controller.C_r = float(scalars[0])
        self.controller.B = float(scalars[1])
        self.controller.freeze_cycles = int(round(float(scalars[2])))
        self.salience.weights = arrays["salience_weights"].astype(np.float64)
        self.salience.previous_error = arrays["salience_previous_error"].astype(np.float64)
        self.value_anchor = QuinaryHypervector(arrays["anchor_sign"], arrays["anchor_mag1"], arrays["anchor_mag2"])
        self.guard = InvariantGuard(self.value_anchor)
        self.coupling.diagonal = arrays["coupling_diagonal"].astype(np.float64)
        self.coupling.basis = arrays["coupling_basis"].astype(np.float64)
        self.coupling.strengths = arrays["coupling_strengths"].astype(np.float64)
        self.coupling.base_alpha, self.coupling.residual = self.coupling._largest_eigenvalue()

        self.memory = WarmMemory()
        for i, record_meta in enumerate(manifest["memory"]):
            vector = QuinaryHypervector(
                arrays["memory_sign"][i], arrays["memory_mag1"][i], arrays["memory_mag2"][i]
            )
            self.memory.add(record_meta["name"], vector, protected=bool(record_meta["protected"]))
            self.memory.records[-1].hits = int(record_meta["hits"])


# =============================================================================
# 8. DEMO, ADVERSARIAL EVENT, AND PROPERTY TESTS
# =============================================================================
def _corrupt_bound_vector(
    vector: QuinaryHypervector,
    binder: QuinaryHypervector,
    *,
    seed: int,
    sign_flips: int,
    erasures: int,
    magnitude_flips: int,
) -> QuinaryHypervector:
    rng = np.random.default_rng(seed)
    q = vector.to_dense()
    b_active = np.flatnonzero(binder.to_dense() != 0)
    active = np.flatnonzero(q != 0)
    if active.size:
        chosen = rng.choice(active, size=min(sign_flips, active.size), replace=False)
        q[chosen] *= -1
    active = np.flatnonzero(q != 0)
    if active.size:
        chosen = rng.choice(active, size=min(erasures, active.size), replace=False)
        q[chosen] = 0
    eligible = np.intersect1d(np.flatnonzero(q != 0), b_active, assume_unique=False)
    if eligible.size:
        chosen = rng.choice(eligible, size=min(magnitude_flips, eligible.size), replace=False)
        q[chosen] = np.sign(q[chosen]) * np.where(np.abs(q[chosen]) == 1, 2, 1)
        # Binding cannot have magnitude 2 when binder magnitude is only 1.
        b = binder.to_dense()
        invalid_high = (np.abs(q) == 2) & (np.abs(b) == 1)
        q[invalid_high] = np.sign(q[invalid_high]).astype(np.int8)
    return QuinaryHypervector.from_dense(q)


def build_demo(seed: int = 2026) -> tuple[NexusRuntime, QuinaryHypervector, QuinaryHypervector]:
    anchor = QuinaryHypervector.random(p_zero=0.65, p_mag2_given_active=0.25, seed=seed + 10)
    runtime = NexusRuntime(seed=seed, value_anchor=anchor)
    runtime.memory.add_random(127, seed=seed + 20, p_zero=0.58)
    constituent = QuinaryHypervector.random(p_zero=0.52, p_mag2_given_active=0.22, seed=seed + 30)
    binder = QuinaryHypervector.random(p_zero=0.18, p_mag2_given_active=0.55, seed=seed + 40)
    runtime.memory.add("TARGET_A", constituent, protected=True)
    return runtime, constituent, binder


def run_demo(seed: int = 2026, snapshot: Optional[Path] = None) -> None:
    runtime, a, b = build_demo(seed)
    expected_c = a.bind(b)
    observed = _corrupt_bound_vector(
        expected_c, b, seed=seed + 50, sign_flips=12, erasures=16, magnitude_flips=10
    )

    print("=" * 96)
    print("PROJECT NEXUS v4.0 — CA/TUCR/HTNLA/MAERA REFERENCE DEMONSTRATOR")
    print("=" * 96)
    print(f"A active={a.popcount} | B active={b.popcount} | expected composite active={expected_c.popcount}")
    print(f"666D base spectral alpha={runtime.coupling.base_alpha:+.6f} residual={runtime.coupling.residual:.2e}")

    normal = runtime.cycle(expected_constituent=a, binder=b, observed_composite=observed)
    print("\n[NOMINAL CYCLE]")
    print(f"stages={normal.stage_trace}")
    print(
        f"bridge: E={normal.bridge.prediction_error:.4f} RPE={normal.bridge.rpe:+.4f} "
        f"Novelty={normal.bridge.novelty:.4f}"
    )
    print(
        f"k-WTA: before={normal.kwta.before} after={normal.kwta.after} pruned={normal.kwta.pruned} "
        f"vacuum={normal.gated_composite.vacuum_fraction:.1%}"
    )
    print(
        f"unbind: exact={normal.partial.exact_count} ambiguous={normal.partial.ambiguous_count} "
        f"unknown={normal.partial.unknown_count} impossible={normal.partial.impossible_count}"
    )
    print(runtime.maera.render(normal))

    stress_observed = _corrupt_bound_vector(
        expected_c, b, seed=seed + 60, sign_flips=45, erasures=70, magnitude_flips=35
    )
    event = HybridEvent(name="PERIMETER_BREACH", severity=1.0)
    stress = runtime.cycle(
        expected_constituent=a,
        binder=b,
        observed_composite=stress_observed,
        event=event,
    )
    print("\n[HYBRID STRESS EVENT]")
    print(
        f"event={stress.controller.event_name} alpha={stress.controller.spectral_alpha:+.4f} "
        f"penalty={stress.controller.spectral_penalty:.2f} k={stress.controller.k_allow} "
        f"fail_safe={stress.controller.fail_safe_triggered}"
    )
    print(runtime.maera.render(stress))

    if snapshot is not None:
        saved = runtime.save_snapshot(snapshot)
        print(f"\nSnapshot written: {saved}")
    print("=" * 96)


def run_self_tests(seed: int = 2026) -> None:
    rng = np.random.default_rng(seed)

    # Vacuum-safe construction and round trip.
    for _ in range(20):
        dense = rng.choice(_ALLOWED_QUINARY, size=DIM).astype(np.int8)
        vector = QuinaryHypervector.from_dense(dense)
        vector.validate()
        assert np.array_equal(vector.to_dense(), dense)

    # Binding contract and partial-inverse admissibility.
    for _ in range(20):
        a = QuinaryHypervector.random(p_zero=0.55, rng=rng)
        b = QuinaryHypervector.random(p_zero=0.35, rng=rng)
        c = a.bind(b)
        assert np.array_equal(c.active, a.active & b.active)
        assert not np.any(c.sign & ~c.active & _FULL_WORD_MASK)
        partial = c.partial_unbind(b)
        assert partial.impossible_count == 0
        assert partial.distance(a) <= EPS

    # Deterministic k-WTA.
    base = QuinaryHypervector.random(p_zero=0.20, seed=seed + 100)
    salience = rng.random(DIM)
    x, y = base.copy(), base.copy()
    rx = x.apply_k_wta(123, salience)
    ry = y.apply_k_wta(123, salience)
    assert rx.after == 123 and ry.after == 123 and x == y

    # Inverse-bridge boundedness, including all-vacuum behavior.
    inverse = InverseBridge()
    memory = WarmMemory()
    zero = QuinaryHypervector.zero()
    anchor = QuinaryHypervector.random(seed=seed + 200)
    signals = inverse.compute(zero, zero, anchor, memory)
    assert signals.prediction_error == 0.0
    assert -1.0 <= signals.rpe <= 1.0
    assert 0.0 <= signals.novelty <= 1.0
    for _ in range(20):
        e = QuinaryHypervector.random(rng=rng)
        a = QuinaryHypervector.random(rng=rng)
        signals = inverse.compute(e, a, anchor, memory)
        assert 0.0 <= signals.prediction_error <= 1.0
        assert -1.0 <= signals.rpe <= 1.0
        assert 0.0 <= signals.novelty <= 1.0

    # Full runtime, target reconstruction, stress fail-safe, snapshot round trip.
    runtime, constituent, binder = build_demo(seed)
    expected_c = constituent.bind(binder)
    observed = _corrupt_bound_vector(expected_c, binder, seed=seed + 300, sign_flips=6, erasures=8, magnitude_flips=5)
    result = runtime.cycle(expected_constituent=constituent, binder=binder, observed_composite=observed)
    assert result.guard.passed
    assert result.snap.accepted and result.snap.name == "TARGET_A"
    stress = runtime.cycle(
        expected_constituent=constituent,
        binder=binder,
        observed_composite=observed,
        event=HybridEvent("TEST_SHOCK", 1.0),
    )
    assert stress.controller.fail_safe_triggered

    temp = Path("/tmp/project_nexus_selftest.qbin")
    runtime.save_snapshot(temp)
    restored = NexusRuntime(seed=seed)
    restored.restore_snapshot(temp)
    assert np.allclose(restored.controller.C, runtime.controller.C)
    assert np.allclose(restored.salience.weights, runtime.salience.weights)
    assert restored.value_anchor == runtime.value_anchor
    assert [r.name for r in restored.memory.records] == [r.name for r in runtime.memory.records]

    # --- Negative tests: the guard and the restore checks must actually reject bad input. ---

    # A guard that has never caught anything is unverified. Corrupt a copy of the
    # controller's own state so it leaves the invariant cube, and confirm the guard
    # flags it rather than only ever seeing legitimate cycles.
    bad_result = runtime.cycle(expected_constituent=constituent, binder=binder, observed_composite=observed)
    sabotaged_controller = ControllerOutput(
        state=np.array([1.4] + [0.5] * 10),  # outside [0, 1]
        cognitive_resource=bad_result.controller.cognitive_resource,
        energy_budget=bad_result.controller.energy_budget,
        k_allow=bad_result.controller.k_allow,
        k_affine=bad_result.controller.k_affine,
        spectral_alpha=bad_result.controller.spectral_alpha,
        spectral_penalty=bad_result.controller.spectral_penalty,
        norm_dcdt=bad_result.controller.norm_dcdt,
        power_demand=bad_result.controller.power_demand,
        fail_safe_triggered=bad_result.controller.fail_safe_triggered,
        frozen=bad_result.controller.frozen,
        event_name=bad_result.controller.event_name,
    )
    sabotaged_report = runtime.guard.audit(
        vector=bad_result.gated_composite,
        anchor=runtime.value_anchor,
        controller=sabotaged_controller,
        partial=bad_result.partial,
    )
    assert not sabotaged_report.passed
    assert any("invariant cube" in v for v in sabotaged_report.violations)

    # A swapped Value Anchor must also be caught, independent of the controller check.
    swapped_anchor = QuinaryHypervector.random(seed=seed + 999)
    anchor_report = runtime.guard.audit(
        vector=bad_result.gated_composite,
        anchor=swapped_anchor,
        controller=bad_result.controller,
        partial=bad_result.partial,
    )
    assert not anchor_report.passed
    assert any("Value Anchor" in v for v in anchor_report.violations)

    # Restore must reject a checksum that no longer matches the payload (tamper detection).
    tampered = Path("/tmp/project_nexus_selftest_tampered.qbin")
    with np.load(temp, allow_pickle=False) as data:
        payload = {k: data[k] for k in data.files}
    manifest = json.loads(bytes(payload["manifest"].tolist()).decode("utf-8"))
    manifest["seed"] = manifest["seed"] + 1  # mutate metadata without recomputing the digest
    payload["manifest"] = np.frombuffer(
        json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode("utf-8"), dtype=np.uint8
    )
    with tampered.open("wb") as fh:
        np.savez_compressed(fh, **payload)
    tamper_rejected = False
    try:
        NexusRuntime(seed=seed).restore_snapshot(tampered)
    except ValueError as exc:
        tamper_rejected = "checksum" in str(exc)
    assert tamper_rejected

    # Restore must reject a snapshot whose calibration fingerprint no longer matches
    # this code's constants, rather than silently running old state under new gains.
    with np.load(temp, allow_pickle=False) as data:
        payload = {k: data[k] for k in data.files}
    manifest = json.loads(bytes(payload["manifest"].tolist()).decode("utf-8"))
    digest = manifest.pop("sha256")
    manifest["calibration_fingerprint"] = "0" * 64
    arrays_only = {k: v for k, v in payload.items() if k != "manifest"}
    manifest["sha256"] = _hash_arrays(arrays_only, manifest)
    payload["manifest"] = np.frombuffer(
        json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode("utf-8"), dtype=np.uint8
    )
    drifted = Path("/tmp/project_nexus_selftest_drifted.qbin")
    with drifted.open("wb") as fh:
        np.savez_compressed(fh, **payload)
    drift_rejected = False
    try:
        NexusRuntime(seed=seed).restore_snapshot(drifted)
    except ValueError as exc:
        drift_rejected = "calibration fingerprint" in str(exc)
    assert drift_rejected

    temp.unlink(missing_ok=True)
    tampered.unlink(missing_ok=True)
    drifted.unlink(missing_ok=True)

    print("All Project Nexus v4.0 property tests passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--self-test", action="store_true", help="run deterministic property tests")
    parser.add_argument("--snapshot", type=Path, default=None, help="write a qbin-like snapshot after the demo")
    args = parser.parse_args()

    if args.self_test:
        run_self_tests(args.seed)
    else:
        run_demo(args.seed, args.snapshot)


if __name__ == "__main__":
    main()
