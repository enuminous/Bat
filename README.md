# BAT

**Baseline Adversarial Tester**

BAT is an EFMW-derived falsification framework whose job is to attack an apparent predictive advantage with strong, simpler conventional explanations.

Its narrow question is:

> Does the candidate signal still add out-of-sample information after strong baselines, matched information access, ablations, shuffled controls, and incremental-feature tests?

BAT is deliberately hostile to the candidate.

## Intended uses

- EFMW benchmark evaluation
- early-warning systems
- anomaly detection
- AI reliability
- control degradation
- forecasting
- network monitoring
- any claimed incremental predictive signal

## Core attack path

```text
candidate claim
→ freeze information set
→ construct strong baselines
→ match train/test access
→ candidate ablations
→ shuffled / placebo controls
→ incremental-feature test
→ calibration comparison
→ BAT verdict
```

## Flat-stack repository

```text
README.md
LICENSE
CITATION.cff
pyproject.toml
requirements.txt
bat.py
models.py
controls.py
metrics.py
freeze.py
verdict_schema.json
example_config.yaml
example_data.csv
example_run.py
test_bat.py
MANIFEST.sha256
```

## Scientific principle

A complicated framework does not earn credit for predicting something already captured by:

- raw state
- signed accumulation
- trend
- rolling moments
- autoregression
- change-point proxies
- calibrated conventional ensembles

The candidate must contribute incremental held-out information.

## Included attacks

1. raw-state logistic baseline
2. signed cumulative-change baseline
3. rolling-statistics baseline
4. autoregressive baseline
5. conventional ensemble
6. candidate-only model
7. baseline + candidate incremental model
8. shuffled-candidate placebo
9. sign ablation
10. recursion ablation

## Primary endpoint

`ΔBrier = Brier(best conventional baseline) - Brier(baseline + candidate)`

Positive values favor incremental candidate utility.

BAT also reports whether the candidate survives the shuffled placebo and whether simpler ablations reproduce the result.

## Verdict logic

- **SURVIVES** — incremental model improves meaningfully and beats placebo.
- **WEAK / INCONCLUSIVE** — tiny or unstable incremental gain.
- **BASELINE EXPLAINS RESULT** — conventional baseline matches or beats candidate.
- **PLACEBO FAILURE** — shuffled candidate performs similarly, suggesting leakage or non-specificity.

The thresholds are examples and must be preregistered for serious studies.

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python example_run.py
```

## Tests

```bash
pytest -q
```

## Freeze discipline

Freeze before labels are exposed:

- candidate formula
- all baseline formulas
- feature access
- prediction horizon
- split
- preprocessing
- hyperparameter search budget
- primary metric
- significance / materiality threshold
- placebo procedure
- ablations
- seeds
- exclusions

Then:

```bash
python freeze.py
```

## Negative results

Negative results are a successful BAT run.

BAT exists to prevent a weak comparison from being mistaken for evidence of a new mechanism.

## Status

Research software. Experimental.
