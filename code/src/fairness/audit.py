from __future__ import annotations
import numpy as np, pandas as pd

def eod(df: pd.DataFrame, group: str, y_col="action", score_col="risk_score", thr=0.6):
    def tpr(d):
        y = d[y_col].astype(int).values
        yhat = (d[score_col].values >= thr).astype(int)
        tp = ((y==1)&(yhat==1)).sum()
        pos = (y==1).sum()
        return tp/max(pos,1)
    g = df[df["subgroup"]==group]
    b = df[df["subgroup"]=="baseline"]
    return float(tpr(g) - tpr(b))

def ece(df: pd.DataFrame, y_col="action", score_col="risk_score", bins=10):
    y = df[y_col].astype(int).values
    p = df[score_col].values
    edges = np.linspace(0,1,bins+1)
    ece = 0.0
    for i in range(bins):
        m = (p>=edges[i]) & (p<edges[i+1])
        if m.sum()==0: continue
        conf = p[m].mean()
        acc  = y[m].mean()
        ece += (m.mean()) * abs(acc - conf)
    return float(ece)

def aer(df: pd.DataFrame, y_col="action", score_col="risk_score", thr=0.6):
    return float(((df[score_col].values>=thr).astype(int)).mean())
