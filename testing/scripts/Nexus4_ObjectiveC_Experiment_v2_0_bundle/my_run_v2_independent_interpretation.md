# Independent interpretation — Nexus 4 Objective C Deep-Time Detector Experiment v2.0

Written after the official run and result hashing, before any detailed reference artifact was opened.

## Independent findings

- Run validity: all built-in self-tests passed; no execution invalidator observed.
- Finite-horizon scenario behavior: every single-channel candidate detects configured creep/instrument/Green-Sky/shock post-onset at 1.00 in this run; crosschannel behaves differently by design and detects instrument/confound while remaining quiet on common-mode creep/Green-Sky/shock.
- Green-Sky: blue-only fixed reference stays anomalous through the plateau; pre-known blue+green bank stays quiet on the plateau, demonstrating recurrence recognition only, not first-time reference authorization.
- Finite-horizon MDR50: CUSUM nu=0.02 is lowest among tested single-channel candidates; raw_sqrt is close but not lowest; leaky candidates are materially worse under this configured ramp/horizon.
- Horizon robustness: raw_fixed fails badly by x4; most empirically fixed-threshold detectors accumulate false alarms as horizon grows. raw_sqrt and normal_mixture_e both remain at 0.03 through x16 in this finite test, but only normal_mixture_e has the modeled time-uniform guarantee and only under the iid Gaussian assumptions.
- Identifiability: creep and instrument channel 1 are bit-identical, so channel-1-only causal attribution is impossible by construction; extra independent information is required.
- Historical predictions: P1/P2/P6/P7/P8 rerun PASS; P3/P4/P5 rerun FAIL, preserving the prior falsifications.
- Post-pilot targets: R1-R6 all PASS on this run.

## Scope boundary

These results characterize this experimental generator/detector suite. They do not establish canonical Nexus subsystem behavior, real THDE severity semantics, reference governance, or architectural ownership without direct source inspection.
