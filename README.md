# Climate RADAR — Reproducible Reference Implementation

This repository provides a lightweight, **fully reproducible** reference implementation of the *Climate RADAR* pipeline:
synthetic data generation, Bayesian-style composite risk modeling with uncertainty, guardrailed recommendation synthesis,
safety-budgeted orchestration, fairness auditing, audit logging, and figure/metric generation — all **offline**.

## Quickstart

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make reproduce
```

Artifacts will appear under `results/` (metrics + figures) and `audit/sample_log.jsonl`.

## Make targets
- `make reproduce` : end-to-end
- `make data`      : regenerate synthetic data
- `make fit`       : fit composite risk model
- `make recs`      : generate recommendations (guardrails + safety budgets)
- `make eval`      : compute AER, EOD (elderly/migrant), ECE
- `make figures`   : save plots (histogram + calibration)

## Docker
```bash
docker build -t climate-radar -f docker/Dockerfile .
docker run --rm -v $PWD:/app climate-radar make reproduce
```

> Educational reference; not for real-world emergency use.
