from __future__ import annotations
import json, time
from pathlib import Path

def append_audit(logfile: Path, event: dict):
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")

def emit_recommendation(row, rec_text: str, repo_hash: str, logfile: Path):
    event = {
        "ts": time.time(),
        "region": row["region"],
        "t": int(row["t"]),
        "risk_score": float(row["risk_score"]),
        "subgroup": row["subgroup"],
        "recommendation": rec_text,
        "repo_hash": repo_hash,
        "version": "0.1.0"
    }
    append_audit(logfile, event)
