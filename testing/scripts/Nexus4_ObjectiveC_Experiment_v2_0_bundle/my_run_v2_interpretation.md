# Nexus 4 Objective C v2.0 Run Interpretation

## Execution provenance

- OS: Linux
- Architecture: x86_64
- Python: 3.14.6 from /home/jmorgan/anaconda3/bin/python3
- NumPy: 2.4.6
- Script SHA-256: `178f5bd650c832ac94172f3009a5189f1b40292f901bd97b4ec32e779a7492be`
- Result SHA-256: `34c4d485ee64fc5ad75381052e7a152b38db9ce1eac259a1c93d49dc73d2be3a`
- Command: `python3 nexus4_leak_blindness_v2_0.py --years 1050 --seeds 40 --calib-seeds 200 --mdr-seeds 32 --horizon-seeds 40 --json my_run_v2.json`

## Independent interpretation before reference comparison

All eight implementation self-tests passed. The current rerun verdicts are P1, P2, P6, P7, and P8 PASS, with P3, P4, and P5 remaining FAIL as their preserved historical predictions require. R1 through R6 all PASS.

The finite-horizon result distinguishes detector behavior but does not establish a canonical Nexus implementation or an infinite-horizon guarantee. `raw_fixed` rises from 0.075 null false-alarm probability at x1 to 1.0 at x4 and x16, showing its base-horizon threshold does not transfer. The Gaussian-mixture e-process is 0.025 at x1, x4, and x16, but that time-uniform result applies only under the modeled iid Gaussian null.

The cross-channel detector is 0.0 for common-mode creep and 1.0 for instrument drift and confound. This demonstrates that additional causally informative information can detect disagreement; it does not identify which channel is truthful.

MDR50 is finite-horizon only. `cusum1_v0.02` is `3.312349219004849e-05` sigma/year and `raw_sqrt` is `5.7608291233894105e-05` sigma/year. The comparison therefore supports R3, but it does not make either detector suitable for an unknown duration.

## Methodological attacks and repairs

- Signal model: a one-dimensional six-sigma linear ramp does not represent high-dimensional cognitive state. Repair: repeat with vector or tensor residuals and source-inspected THDE severity mappings.
- Null model: iid Gaussian noise excludes autocorrelation, heavy tails, and variance drift. Repair: run separately named AR(1), Student-t, seasonal, and regime-switching null experiments.
- Calibration: 200 calibration seeds quantize the target false-alarm rate. Repair: increase calibration and horizon seed counts and report confidence intervals.
- Horizon test: x16 remains finite. Repair: sweep further horizons while retaining an anytime-valid control under explicitly tested assumptions.
- Identifiability: two channels can share a failure mode. Repair: model correlated sensor, calibration, and provenance failures before claiming attribution capability.
- Reference semantics: a pre-known reference bank is recurrence recognition only. Repair: test separate candidate retention, evidence validation, authorization, promotion, and retirement policies.
- Architectural transfer: this research harness does not establish Nexus subsystem behavior. Repair: inspect and cite the actual source for severity mapping, state geometry, hysteresis, retention, and ownership before proposing integration.