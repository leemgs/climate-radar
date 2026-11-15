from __future__ import annotations
import numpy as np, pandas as pd
from dataclasses import dataclass

@dataclass
class Posterior:
    coef_mean: np.ndarray
    coef_cov: np.ndarray

def bayes_linear_posterior(X: np.ndarray, y: np.ndarray, sigma2: float=0.10, tau2: float=2.0) -> Posterior:
    XtX = X.T @ X
    A = XtX / sigma2 + np.eye(X.shape[1]) / tau2
    A_inv = np.linalg.inv(A)
    mu = A_inv @ (X.T @ y) / sigma2
    cov = A_inv
    return Posterior(coef_mean=mu, coef_cov=cov)

def predict_posterior(X: np.ndarray, post: Posterior):
    mean = X @ post.coef_mean
    var = np.sum((X @ post.coef_cov) * X, axis=1)
    return mean, var

def fit_composite_risk(df: pd.DataFrame):
    X = df[["hazard","exposure","vulnerability","social"]].to_numpy().copy()
    X[:,2] = 1.0 - X[:,2]  # invert vulnerability
    X = np.c_[np.ones(len(X)), X]
    y = df["action"].astype(float).to_numpy()
    post = bayes_linear_posterior(X, y, sigma2=0.10, tau2=2.0)
    mean, var = predict_posterior(X, post)
    risk = np.clip(mean, 0, 1)
    df2 = df.copy()
    df2["risk_score"] = risk
    df2["risk_var"] = var
    return df2, post
