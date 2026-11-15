from __future__ import annotations
import pandas as pd
from typing import Dict
from .guardrails import sanitize, glossary_expand

def recommend(row: pd.Series, cfg: Dict) -> str:
    r = row["risk_score"]
    sub = row["subgroup"]
    th = cfg["thresholds"]["risk_thresholds"]
    if r >= th["high"]:
        rec = "IMMEDIATE: Move to nearest shelter; bring ID, water, and phone."
    elif r >= th["medium"]:
        rec = "PREPARE: Pack essentials, confirm route to shelter, check on neighbors."
    else:
        rec = "STAY ALERT: Monitor updates; avoid low-lying areas."
    if sub == "elderly":
        rec += " If mobility is limited, call local support or ask a neighbor for assistance."
    if sub == "migrant":
        rec += " Multilingual help is available at the community center."
    rec = glossary_expand(rec, cfg["policy"].get("jargon_glossary", []))
    rec = sanitize(rec, cfg["policy"].get("deny_terms", []))
    return rec
