from __future__ import annotations
import hashlib, yaml
from pathlib import Path
from dataclasses import dataclass

ROOT = Path(__file__).resolve().parents[1]

def _load_yaml(p: Path):
    with open(p, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def _repo_hash() -> str:
    h = hashlib.sha256()
    for p in sorted((ROOT/"configs").glob("*.yaml")):
        h.update(p.read_bytes())
    return h.hexdigest()[:12]

@dataclass
class Config:
    policy: dict
    thresholds: dict
    experiments: dict
    repo_hash: str

def load_config() -> Config:
    policy = _load_yaml(ROOT/"configs"/"policy.yaml")
    thresholds = _load_yaml(ROOT/"configs"/"thresholds.yaml")
    experiments = _load_yaml(ROOT/"configs"/"experiments.yaml")
    return Config(policy=policy, thresholds=thresholds, experiments=experiments, repo_hash=_repo_hash())
