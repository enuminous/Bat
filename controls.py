import numpy as np
import pandas as pd

def raw_state(df, cols):
    return df[cols].astype(float).ffill().fillna(0.0)

def signed_accumulator(df, cols):
    x=raw_state(df,cols)
    dx=x.diff().fillna(0.0)
    return pd.DataFrame({
        "signed_accumulator":dx.mean(axis=1).cumsum(),
        "signed_change":dx.mean(axis=1),
    })

def rolling_stats(df, cols, window=23):
    x=raw_state(df,cols)
    return pd.DataFrame({
        "rolling_mean":x.rolling(window,min_periods=1).mean().mean(axis=1),
        "rolling_std":x.rolling(window,min_periods=2).std().mean(axis=1).fillna(0.0),
        "rolling_abs_change":x.diff().abs().rolling(window,min_periods=1).mean().mean(axis=1).fillna(0.0),
    }).fillna(0.0)

def autoregressive(df, cols, lags=(1,2,3,7)):
    x=raw_state(df,cols)
    out={}
    for c in cols:
        out[c]=x[c]
        for lag in lags:
            out[f"{c}__lag{lag}"]=x[c].shift(lag).fillna(0.0)
    return pd.DataFrame(out,index=df.index)

def candidate_features(df, cols):
    x=raw_state(df,cols)
    dx=x.diff().fillna(0.0)
    signed=dx.mean(axis=1)
    disagreement=x.std(axis=1).fillna(0.0)
    velocity=disagreement.diff().fillna(0.0)
    recursive=np.zeros(len(df))
    for i in range(len(df)):
        prev=recursive[i-1] if i else 0.0
        base=float(disagreement.iloc[i] + abs(signed.iloc[i]))
        recursive[i]=0.65*prev+0.35*np.tanh(base)
    return pd.DataFrame({
        "candidate_signed":signed,
        "candidate_disagreement":disagreement,
        "candidate_velocity":velocity,
        "candidate_recursive":recursive,
        "candidate_score":(
            signed.abs().rank(pct=True)
            +disagreement.rank(pct=True)
            +velocity.abs().rank(pct=True)
            +pd.Series(recursive,index=df.index).rank(pct=True)
        )/4.0
    },index=df.index)

def sign_ablation(candidate):
    out=candidate.copy()
    out["candidate_signed"]=out["candidate_signed"].abs()
    return out

def recursion_ablation(candidate):
    return candidate.drop(columns=["candidate_recursive"],errors="ignore")

def shuffled_candidate(candidate, seed=23):
    rng=np.random.default_rng(seed)
    idx=rng.permutation(len(candidate))
    arr=candidate.to_numpy()[idx]
    return pd.DataFrame(arr,index=candidate.index,columns=candidate.columns)
