from dataclasses import dataclass
import pandas as pd
from models import LogisticModel
from controls import (
    raw_state,signed_accumulator,rolling_stats,autoregressive,
    candidate_features,sign_ablation,recursion_ablation,shuffled_candidate
)
from metrics import binary_metrics

@dataclass
class BATExperiment:
    time_column: str
    target_column: str
    feature_columns: list
    train_fraction: float = 0.65
    random_state: int = 23
    material_brier_gain: float = 0.002

    def _fit_eval(self,X,y,cut):
        m=LogisticModel(self.random_state)
        m.fit(X.iloc[:cut],y[:cut])
        p=m.predict_proba(X.iloc[cut:])
        return binary_metrics(y[cut:],p)

    def run(self,df):
        df=df.sort_values(self.time_column).reset_index(drop=True).copy()
        y=df[self.target_column].astype(int).to_numpy()
        cut=max(30,int(len(df)*self.train_fraction))

        raw=raw_state(df,self.feature_columns)
        signed=signed_accumulator(df,self.feature_columns)
        rolling=rolling_stats(df,self.feature_columns)
        ar=autoregressive(df,self.feature_columns)
        cand=candidate_features(df,self.feature_columns)

        conventional={
            "raw_state":raw,
            "signed_accumulator":signed,
            "rolling_stats":rolling,
            "autoregressive":ar,
            "conventional_ensemble":pd.concat([raw,signed,rolling,ar],axis=1),
        }

        results={}
        for name,X in conventional.items():
            results[name]=self._fit_eval(X,y,cut)

        best_name=min(conventional,key=lambda n:results[n]["brier"])
        best=conventional[best_name]

        attacks={
            "candidate_only":cand,
            "best_baseline_plus_candidate":pd.concat([best,cand],axis=1),
            "best_baseline_plus_shuffled_candidate":pd.concat([
                best,shuffled_candidate(cand,self.random_state)
            ],axis=1),
            "best_baseline_plus_sign_ablation":pd.concat([best,sign_ablation(cand)],axis=1),
            "best_baseline_plus_recursion_ablation":pd.concat([best,recursion_ablation(cand)],axis=1),
        }

        for name,X in attacks.items():
            results[name]=self._fit_eval(X,y,cut)

        base_brier=results[best_name]["brier"]
        inc_brier=results["best_baseline_plus_candidate"]["brier"]
        placebo_brier=results["best_baseline_plus_shuffled_candidate"]["brier"]
        gain=base_brier-inc_brier
        placebo_gain=base_brier-placebo_brier

        if placebo_gain >= gain - 1e-6 and gain > 0:
            verdict="PLACEBO FAILURE"
        elif gain >= self.material_brier_gain and inc_brier < placebo_brier:
            verdict="SURVIVES"
        elif gain > 0 and inc_brier < placebo_brier:
            verdict="WEAK / INCONCLUSIVE"
        else:
            verdict="BASELINE EXPLAINS RESULT"

        return {
            "n_total":len(df),
            "train_n":cut,
            "test_n":len(df)-cut,
            "best_conventional_baseline":best_name,
            "results":results,
            "primary_delta_brier_best_baseline_minus_incremental":gain,
            "placebo_delta_brier_best_baseline_minus_shuffled":placebo_gain,
            "materiality_threshold":self.material_brier_gain,
            "verdict":verdict,
            "interpretation":"BAT rewards only incremental held-out information that survives strong conventional and placebo attacks."
        }
