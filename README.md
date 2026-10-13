# BAT

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Bat) · This repository is linked through its source; GitHub Pages is not enabled.

<details>
<summary>Recent repositories (9)</summary>

- [Oroboros](https://github.com/enuminous/Oroboros) · [README](https://github.com/enuminous/Oroboros/blob/main/README.md) · [Page](https://enuminous.github.io/Oroboros/)
- [P-NP](https://github.com/enuminous/P-NP) · [README](https://github.com/enuminous/P-NP/blob/main/README.md) · [Page](https://enuminous.github.io/P-NP/)
- [Research-Program](https://github.com/enuminous/Research-Program) · [README](https://github.com/enuminous/Research-Program/blob/main/README.md) · [Page](https://enuminous.github.io/Research-Program/)
- [I-Have-Guts](https://github.com/enuminous/I-Have-Guts) · [README](https://github.com/enuminous/I-Have-Guts/blob/main/README.md) · [Page](https://enuminous.github.io/I-Have-Guts/)
- [Wrights-Law](https://github.com/enuminous/Wrights-Law) · [README](https://github.com/enuminous/Wrights-Law/blob/main/README.md) · [Page](https://enuminous.github.io/Wrights-Law/)
- [Aristotle-eNuminous](https://github.com/enuminous/Aristotle-eNuminous) · [README](https://github.com/enuminous/Aristotle-eNuminous/blob/main/README.md) · [Page](https://enuminous.github.io/Aristotle-eNuminous/)
- [Multiverse-Simulator](https://github.com/enuminous/Multiverse-Simulator) · [README](https://github.com/enuminous/Multiverse-Simulator/blob/main/README.md) · [Page](https://enuminous.github.io/Multiverse-Simulator/)
- [accelerando-8192](https://github.com/enuminous/accelerando-8192) · [README](https://github.com/enuminous/accelerando-8192/blob/main/README.md) · [Page source](https://github.com/enuminous/accelerando-8192/blob/main/docs/index.html)
- [Codex-888](https://github.com/enuminous/Codex-888) · [README](https://github.com/enuminous/Codex-888/blob/main/README.md) · [Page](https://enuminous.github.io/Codex-888/)

</details>
<!-- ENUMINOUS-NETWORK:END -->

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
