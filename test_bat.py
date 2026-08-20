import pandas as pd
from bat import BATExperiment
from controls import candidate_features, shuffled_candidate

FEATURES=["signal_a","signal_b","signal_c"]

def test_placebo_is_permutation():
    df=pd.read_csv("example_data.csv")
    c=candidate_features(df,FEATURES)
    s=shuffled_candidate(c,23)
    assert c.shape==s.shape
    assert abs(c["candidate_score"].sum()-s["candidate_score"].sum())<1e-9

def test_bat_runs_and_verdict_valid():
    df=pd.read_csv("example_data.csv")
    out=BATExperiment(
        time_column="time",
        target_column="future_event",
        feature_columns=FEATURES,
    ).run(df)
    assert out["verdict"] in {
        "SURVIVES","WEAK / INCONCLUSIVE",
        "BASELINE EXPLAINS RESULT","PLACEBO FAILURE"
    }
    assert "best_conventional_baseline" in out
    assert "primary_delta_brier_best_baseline_minus_incremental" in out
