# CA TUCR HTLA Continuous to Discrete Bridge Formalization

## Executive assessment

Your July 18 test log already established the important architectural fact: the continuous layer can drive a scalar sparsity gate that performs a k-WTA wipeout on the 1024D quinary substrate, while the masking rule enforces the invariant $P_A=0 \Rightarrow P_S=0$ even under an injected shock. The same log also made the remaining gaps explicit: no ratified $dC_r/dt$, no ratified 666D-to-threshold reduction, and no ratified nontrivial $W_C, W_E, W_R, W_N, \Lambda$. The recommendations below preserve the documented structure and replace only those three open placeholders with bounded, executable mathematics.

The proposal keeps the existing ODE skeleton and the existing k-WTA bridge, but makes the bridge mathematically tighter in three ways. First, cognitive resources become a bounded leaky integrator slaved to an explicit energy-budget variable, which makes the 85% cap exact rather than aspirational. Second, the 666D coupling contribution becomes a spectral friction term driven by the dominant real growth mode of the coupling matrix, with a conservative non-normality guard. Third, the 11D coupling matrices are instantiated as normalized neurocomputational gains consistent with the best-supported directional motifs in the literature: reward-prediction-error strongly drives dopamine; novelty drives norepinephrine and acetylcholine; fast error drive is routed through glutamatergic excitation; GABA supplies distributed inhibition; serotonin contributes a net stabilizing and suppressive influence on runaway excitation and internal gain.

## Resource dynamics

A resource law for this architecture has to do two jobs at once. It has to act like a slow allostatic reserve, because brains regulate behavior under finite energetic constraints, and it has to crash hard when surprise and state-velocity spike, because those are exactly the conditions that should tighten the Lyapunov fail-safe. The neuroscience side of that choice is well motivated: signaling is metabolically expensive, the brain operates under a finite energy budget, and predictive/allostatic regulation is fundamentally about matching energetic supply to anticipated demand.

Introduce one auxiliary scalar $B(t)$, the **remaining admissible expendable budget**, with $0 \le B(t) \le 0.85E_{\max}$, and define $C_r(t)$ as a filtered accessibility of that budget rather than the budget itself. Let

$$
p(t)=\alpha_C \,\|\dot C(t)\|_2^2+\alpha_R\,RPE(t)^2+\alpha_N\,Novelty(t)^2
$$

with normalized gains

$$
\alpha_C=0.25,\qquad \alpha_R=0.18,\qquad \alpha_N=0.14.
$$

Then evolve the budget by

$$
\dot B(t)= -\,\frac{p(t)}{0.85E_{\max}}\,B(t), \qquad B(0)=0.85E_{\max}.
$$

Define the resource state directly as

$$
\dot C_r(t)=
\rho\!\left(0.05+0.95\frac{B(t)}{0.85E_{\max}}-C_r(t)\right)
-
p(t)\,\big(C_r(t)-0.05\big),
$$

with

$$
\rho=0.08,\qquad C_r(t)\in[0.05,1].
$$

This is the proposed ratified $dC_r/dt$. It is a true leaky integrator because the first term relaxes $C_r$ toward the budget-limited ceiling $0.05+0.95B/(0.85E_{\max})$, while the second term depletes accessible resources proportionally to instantaneous energetic demand. Because $p(t)$ depends on both $\|\dot C\|_2^2$ and the squared shock variables, the law naturally crashes under large RPE and novelty spikes, which is exactly the behavior the failure protocol wants.

Two invariants follow. If $C_r=0.05$, then

$$
\dot C_r=\rho\!\left(0.95\frac{B}{0.85E_{\max}}\right)\ge 0,
$$

so the floor is forward invariant. If $C_r=1$, then the relaxation term is nonpositive and the depletion term is strictly nonpositive, so $\dot C_r\le 0$, which makes the ceiling forward invariant.

The 85% budget cap is exact:

$$
\int_0^T \left(-\dot B(t)\right)\,dt=B(0)-B(T)\le 0.85E_{\max}.
$$

Therefore the architecture cannot admit more than $0.85E_{\max}$ of expendable bridge energy over the episode encoded by $B$.

## Spectral friction law

For the 666D coupling term, an RMS norm is not the relevant dynamical object. In continuous-time systems, instability is governed by the dominant real growth mode. Let the 666D coupling object be a real square matrix $M\in\mathbb{R}^{666\times 666}$. Define the spectral-abscissa term

$$
\alpha(M)=\max_i \operatorname{Re}\lambda_i(M).
$$

Because highly non-normal matrices can transiently amplify even when $\alpha(M)<0$, include a conservative guard term based on the symmetric part,

$$
\mu_2(M)=\lambda_{\max}\!\left(\frac{M+M^\top}{2}\right),
$$

and define the effective resonance score

$$
\widehat\alpha(M)=\max\{\alpha(M),\mu_2(M)\}.
$$

This reacts both to a genuinely unstable dominant eigenmode and to matrices whose symmetric part can produce large Euclidean growth before asymptotic decay settles in. The scalar friction penalty is

$$
\Pi_M
=
\gamma_M\left(\exp\!\big(\beta_M[\widehat\alpha(M)]_+\big)-1\right),
\qquad [x]_+=\max(x,0),
$$

with

$$
\gamma_M=28,\qquad \beta_M=2.4.
$$

When the dominant mode is stable, $\widehat\alpha(M)\le 0$, the friction vanishes. Once the dominant mode crosses into positive growth, the penalty rises exponentially rather than linearly, violently tightening the gate against runaway resonance. For reference, $\widehat\alpha=0.5$ produces a penalty of about 65 active coordinates, while $\widehat\alpha=1.0$ produces about 281, nearly choking the legal 307-coordinate active ceiling by itself.

Preserving the documented 11D affine gate form,

$$
k_{11D}(t)=
k_0+a\,DA(t)-b\,5HT(t)-c\,GABA(t)-d\,Temp(t),
$$

with normalized coefficients

$$
k_0=256,\qquad a=96,\qquad b=64,\qquad c=72,\qquad d=32,
$$

and

$$
k_{\text{allow}}(t)=
\left\lfloor
\operatorname{clip}\!\big(k_{11D}(t)-\Pi_M,\;1,\;307\big)
\right\rfloor.
$$

The fail-safe remains as documented: if $\|\dot C\|_2>5C_r$, halve $k_{\text{allow}}$ again after applying the spectral penalty.

## Cross-coupling matrices

The 11-state order is

$$
[NE,\;DA,\;5HT,\;ACh,\;Glu,\;GABA,\;Perception,\;Cognition,\;Affect,\;Volition,\;Self]^\top.
$$

The guiding biological motifs are: dopamine is the canonical reward-prediction-error teaching signal and should be the strongest direct recipient of RPE input; novelty and unexpected uncertainty recruit norepinephrine and acetylcholine strongly; glutamate is the principal fast excitatory transmitter and carries external error drive into perceptual and cognitive state variables; GABA supplies broad inhibitory balancing pressure; serotonin is not universally inhibitory across receptor classes, but at this architecture level acts as a net stabilizing influence on spontaneous gain, excitatory throughput, and affective volatility, with a modest positive contribution to self-stability. Acetylcholine and norepinephrine positively bias perception, attention, and cognition rather than raw affective amplification. Dopamine enhances cognition and volition, but remains restrained to avoid loss of prefrontal stability.

The leak matrix is diagonal and intentionally stronger than 1 on every channel so that $C_i=1$ always points inward while $C_i=0$ always points inward, making the state cube forward invariant without altering the ODE form:

$$
\Lambda=\operatorname{diag}(1.30,\;1.25,\;1.20,\;1.25,\;1.35,\;1.35,\;1.15,\;1.10,\;1.15,\;1.10,\;1.05).
$$

The three scalar-input gain vectors are

$$
w_E=
\begin{bmatrix}
0.20\\
0.05\\
0.00\\
0.20\\
1.00\\
0.25\\
0.70\\
0.45\\
0.10\\
0.10\\
-0.05
\end{bmatrix},
\qquad
w_R=
\begin{bmatrix}
0.20\\
1.00\\
-0.15\\
0.05\\
0.25\\
0.10\\
0.00\\
0.30\\
0.55\\
0.35\\
0.10
\end{bmatrix},
\qquad
w_N=
\begin{bmatrix}
1.00\\
0.20\\
-0.05\\
0.95\\
0.30\\
0.05\\
0.40\\
0.25\\
0.15\\
0.10\\
-0.10
\end{bmatrix}.
$$

Equivalently, $W_E=\operatorname{diag}(w_E)$, $W_R=\operatorname{diag}(w_R)$, and $W_N=\operatorname{diag}(w_N)$. These choices satisfy the hard constraints: high RPE most strongly drives $DA$; high novelty most strongly drives $ACh$ and $NE$; $E_{err}$ most strongly drives $Glu$; inhibitory balancing is carried by $GABA$ and net-serotonergic suppression.

The recurrent state-coupling matrix $W_C$ is given below. Rows are targets and columns are sources in the state order above.

```python
W_C = np.array([
    [ 0.05,  0.00, -0.08,  0.08,  0.10, -0.12,  0.10,  0.06,  0.08,  0.06,  0.00],  # NE
    [ 0.06,  0.08, -0.12,  0.02,  0.05, -0.10,  0.00,  0.10,  0.18,  0.16,  0.08],  # DA
    [-0.04, -0.06,  0.10,  0.00, -0.08,  0.10, -0.02,  0.00, -0.06, -0.04,  0.12],  # 5HT
    [ 0.12,  0.00, -0.04,  0.08,  0.10, -0.08,  0.14,  0.12,  0.00,  0.04, -0.02],  # ACh
    [ 0.06,  0.08, -0.10,  0.06,  0.10, -0.16,  0.12,  0.14,  0.08,  0.10,  0.00],  # Glu
    [-0.02, -0.02,  0.10, -0.02,  0.12,  0.06,  0.00,  0.00,  0.05, -0.02,  0.04],  # GABA
    [ 0.16,  0.02, -0.06,  0.18,  0.18, -0.12,  0.12,  0.12,  0.00,  0.00, -0.04],  # Perception
    [ 0.10,  0.12,  0.00,  0.10,  0.14, -0.10,  0.18,  0.16,  0.05,  0.12,  0.08],  # Cognition
    [ 0.18,  0.10,  0.12,  0.00,  0.05, -0.18,  0.04,  0.04,  0.12,  0.12,  0.10],  # Affect
    [ 0.08,  0.18, -0.04,  0.02,  0.12, -0.10,  0.00,  0.16,  0.16,  0.16,  0.08],  # Volition
    [ 0.04,  0.08,  0.16,  0.00,  0.00, -0.10,  0.02,  0.08,  0.12,  0.14,  0.18],  # Self
], dtype=float)
```

These are **normalized architecture coefficients**, not claims about literal synaptic efficacies in vivo. The ratification claim is narrower: the signs and relative magnitudes follow validated neurocomputational directionality, while the absolute scale is deliberately chosen to satisfy the global contraction inequality of the bounded sigmoidal ODE.

## Stability and bounded energy proof

For the 11D ODE,

$$
\dot C = -\Lambda C + \sigma(W_CC+w_EE_{err}+w_RRPE+w_NNovelty+b),
$$

the logistic nonlinearity is globally Lipschitz with constant $L_\sigma=\tfrac14$. For two trajectories $C_1,C_2$, let $\Delta=C_1-C_2$ and $V=\tfrac12\|\Delta\|_2^2$. Then

$$
\dot V
\le
-\left(\lambda_{\min}(\Lambda)-\frac14\|W_C\|_2\right)\,\|\Delta\|_2^2.
$$

A sufficient condition for global exponential contraction is

$$
\lambda_{\min}(\Lambda)>\frac14\|W_C\|_2.
$$

With the matrix above, $\lambda_{\min}(\Lambda)=1.05$ and $\|W_C\|_2\approx0.867$, so the contraction margin is about $0.833>0$.

Boundedness is stronger than contraction here. Because $\sigma(\cdot)\in(0,1)$, every coordinate satisfies

$$
\dot C_i\ge 0 \quad \text{at } C_i=0,
\qquad
\dot C_i\le -\lambda_i+1<0 \quad \text{at } C_i=1,
$$

since every $\lambda_i>1$. Therefore the cube $[0,1]^{11}$ is forward invariant.

For the resource law, boundedness follows from the boundary derivatives. The energy guarantee is exact because

$$
-\dot B(t)=\frac{p(t)}{0.85E_{\max}}B(t)\ge0
$$

and hence

$$
\int_0^T\left(-\dot B(t)\right)dt=B(0)-B(T)\le0.85E_{\max}.
$$

For the 666D term, using $\widehat\alpha(M)$ means that any coupling mode with positive real growth immediately produces a monotone increase in $\Pi_M$. Because the penalty is exponential in $[\widehat\alpha(M)]_+$, the gate becomes sharply more restrictive exactly when the coupling layer is closest to unstable amplification.

## NumPy reference implementation

The code below implements one timestep of the proposed formulas and returns the updated $C_r$ and finalized integer $k_{\text{allow}}$. It preserves the bounded 11D ODE, affine 11D sparsity gate, spectral 666D penalty, and fail-safe trigger $\|\dot C\|_2>5C_r$.

```python
import numpy as np


def sigma(x: np.ndarray) -> np.ndarray:
    """Logistic activation."""
    return 1.0 / (1.0 + np.exp(-x))


# State order:
# [NE, DA, 5HT, ACh, Glu, GABA, Perception, Cognition, Affect, Volition, Self]

LAMBDA = np.diag([
    1.30, 1.25, 1.20, 1.25, 1.35, 1.35, 1.15, 1.10, 1.15, 1.10, 1.05
]).astype(float)

W_C = np.array([
    [ 0.05,  0.00, -0.08,  0.08,  0.10, -0.12,  0.10,  0.06,  0.08,  0.06,  0.00],
    [ 0.06,  0.08, -0.12,  0.02,  0.05, -0.10,  0.00,  0.10,  0.18,  0.16,  0.08],
    [-0.04, -0.06,  0.10,  0.00, -0.08,  0.10, -0.02,  0.00, -0.06, -0.04,  0.12],
    [ 0.12,  0.00, -0.04,  0.08,  0.10, -0.08,  0.14,  0.12,  0.00,  0.04, -0.02],
    [ 0.06,  0.08, -0.10,  0.06,  0.10, -0.16,  0.12,  0.14,  0.08,  0.10,  0.00],
    [-0.02, -0.02,  0.10, -0.02,  0.12,  0.06,  0.00,  0.00,  0.05, -0.02,  0.04],
    [ 0.16,  0.02, -0.06,  0.18,  0.18, -0.12,  0.12,  0.12,  0.00,  0.00, -0.04],
    [ 0.10,  0.12,  0.00,  0.10,  0.14, -0.10,  0.18,  0.16,  0.05,  0.12,  0.08],
    [ 0.18,  0.10,  0.12,  0.00,  0.05, -0.18,  0.04,  0.04,  0.12,  0.12,  0.10],
    [ 0.08,  0.18, -0.04,  0.02,  0.12, -0.10,  0.00,  0.16,  0.16,  0.16,  0.08],
    [ 0.04,  0.08,  0.16,  0.00,  0.00, -0.10,  0.02,  0.08,  0.12,  0.14,  0.18],
], dtype=float)

# Scalar-input gain vectors; equivalent to diagonal matrices W_E, W_R, W_N
W_E = np.array([0.20, 0.05, 0.00, 0.20, 1.00, 0.25, 0.70, 0.45, 0.10, 0.10, -0.05], dtype=float)
W_R = np.array([0.20, 1.00, -0.15, 0.05, 0.25, 0.10, 0.00, 0.30, 0.55, 0.35, 0.10], dtype=float)
W_N = np.array([1.00, 0.20, -0.05, 0.95, 0.30, 0.05, 0.40, 0.25, 0.15, 0.10, -0.10], dtype=float)

# Basal offset
BIAS = np.array([0.10, 0.08, 0.12, 0.10, 0.05, 0.10, 0.08, 0.10, 0.06, 0.06, 0.08], dtype=float)

# Resource-law gains
ALPHA_C = 0.25
ALPHA_R = 0.18
ALPHA_N = 0.14
RHO_CR = 0.08

# 11D sparsity gate coefficients; keeps the documented affine form
K0 = 256.0
A_DA = 96.0
B_5HT = 64.0
C_GABA = 72.0
D_TEMP = 32.0

# Spectral friction gains
GAMMA_M = 28.0
BETA_M = 2.4


def coupling_penalty(M: np.ndarray) -> tuple[float, float]:
    """
    Return (effective_resonance_score, scalar_penalty).

    Uses:
      alpha(M)  = max Re(lambda_i(M))
      mu2(M)    = lambda_max((M + M.T)/2)
      alpha_hat = max(alpha, mu2)

    The second term is a conservative non-normality guard.
    """
    if M.ndim != 2 or M.shape[0] != M.shape[1]:
        raise ValueError("M must be a square 2D NumPy array.")

    alpha = float(np.max(np.real(np.linalg.eigvals(M))))
    mu2 = float(np.max(np.linalg.eigvalsh((M + M.T) / 2.0)))
    alpha_hat = max(alpha, mu2)

    penalty = GAMMA_M * (np.exp(BETA_M * max(alpha_hat, 0.0)) - 1.0)
    return alpha_hat, float(penalty)


def bridge_timestep(
    C: np.ndarray,
    C_r: float,
    budget_B: float,
    M: np.ndarray,
    E_err: float,
    RPE: float,
    Novelty: float,
    dt: float = 0.02,
    E_max: float = 1.0,
) -> tuple[np.ndarray, float, float, int, dict]:
    """
    Execute one bridge timestep.

    Parameters
    ----------
    C : (11,) array
        Current continuous state in [0, 1]^11.
    C_r : float
        Cognitive resources in [0.05, 1.0].
    budget_B : float
        Remaining expendable bridge budget in [0, 0.85 * E_max].
    M : (666, 666) array
        Continuous coupling/intermodulation matrix.
    E_err, RPE, Novelty : float
        Scalar drives.
    dt : float
        Integration timestep.
    E_max : float
        Resource budget scale.

    Returns
    -------
    C_next : np.ndarray
    C_r_next : float
    budget_B_next : float
    k_allow : int
    diagnostics : dict
    """
    C = np.asarray(C, dtype=float).reshape(-1)
    if C.shape[0] != 11:
        raise ValueError("C must have shape (11,).")
    if not (0.05 <= C_r <= 1.0):
        raise ValueError("C_r must be in [0.05, 1.0].")
    if budget_B < 0.0 or budget_B > 0.85 * E_max:
        raise ValueError("budget_B must be in [0, 0.85 * E_max].")

    # Continuous ODE
    drive = W_C @ C + W_E * E_err + W_R * RPE + W_N * Novelty + BIAS
    dCdt = -LAMBDA @ C + sigma(drive)
    C_next = np.clip(C + dt * dCdt, 0.0, 1.0)

    # Energy / resource dynamics
    p = (
        ALPHA_C * float(np.dot(dCdt, dCdt))
        + ALPHA_R * float(RPE ** 2)
        + ALPHA_N * float(Novelty ** 2)
    )

    # Exact 85% budget law
    dBdt = -(p / (0.85 * E_max)) * budget_B
    budget_B_next = float(np.clip(budget_B + dt * dBdt, 0.0, 0.85 * E_max))

    # Cognitive resource law
    budget_ceiling = 0.05 + 0.95 * (budget_B / (0.85 * E_max))
    dCrdt = RHO_CR * (budget_ceiling - C_r) - p * (C_r - 0.05)
    C_r_next = float(np.clip(C_r + dt * dCrdt, 0.05, 1.0))

    # 11D gate
    DA = float(C_next[1])
    HT5 = float(C_next[2])
    GABA = float(C_next[5])
    Temp = 1.0 - float(C_next[8])  # preserved from the existing bridge formula

    k_11D = K0 + A_DA * DA - B_5HT * HT5 - C_GABA * GABA - D_TEMP * Temp

    # 666D spectral friction
    alpha_hat, penalty_M = coupling_penalty(M)

    # Final threshold before fail-safe
    k_allow = int(np.clip(np.floor(k_11D - penalty_M), 1, 307))

    # Documented Lyapunov fail-safe
    norm_dCdt = float(np.linalg.norm(dCdt))
    unstable = norm_dCdt > (5.0 * C_r_next)
    if unstable:
        k_allow = max(1, int(np.floor(0.5 * k_allow)))

    diagnostics = {
        "drive": drive,
        "dCdt": dCdt,
        "power_p": p,
        "budget_ceiling": budget_ceiling,
        "k_11D": float(k_11D),
        "alpha_hat": alpha_hat,
        "penalty_M": penalty_M,
        "norm_dCdt": norm_dCdt,
        "unstable": unstable,
    }
    return C_next, C_r_next, budget_B_next, k_allow, diagnostics
```

## Ratification boundary

This implementation is the minimal bridge proposed for sign-off. It preserves the already-verified discrete masking invariant, gives an exact $dC_r/dt$ with an exact 85% energy cap, converts the 666D layer into a spectral friction law rather than an RMS placeholder, and instantiates the 11D ODE couplings with explicit normalized weights that are both biologically legible and Lyapunov-safe.

The numerical coefficients remain architecture-level normalized design values, not literal biological synaptic measurements. They should be subjected to the same 40-step shock test, followed by Monte Carlo, non-normal transient-growth, timestep-sensitivity, and ablation testing before being treated as production constants.
