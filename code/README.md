# Climate RADAR — Reproducible Reference Implementation

A lightweight, offline, reproducible reference implementation of the Climate RADAR pipeline: synthetic data generation, Bayesian-style composite risk modeling with uncertainty, guardrailed recommendation synthesis, safety-budgeted orchestration, fairness auditing, audit logging, and figure/metric generation.

> Educational reference; not for real-world emergency use. The data are synthetic.

## Layout

```
code/
├── Makefile               # make reproduce (run from this folder)
├── requirements.txt
├── configs/               # policy.yaml, thresholds.yaml, experiments.yaml
├── data/synthetic/        # generated synthetic time series
├── src/                   # pipeline modules (model, llm guardrails, orchestration, fairness, reproducibility)
├── scripts/               # helpers that print metrics / list figures
├── docker/Dockerfile      # build from the repository root
└── results_quicklook.ipynb
```

Outputs are written to [`../artifact/`](../artifact/): `results/` (metrics and figures) and `audit/sample_log.jsonl`.

## Quickstart

```bash
cd code
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make reproduce
```

## Make targets
- `make reproduce`: end to end
- `make data`: regenerate synthetic data
- `make fit`: fit the composite risk model
- `make recs`: generate recommendations (guardrails + safety budgets)
- `make eval`: compute AER, EOD (elderly/migrant), ECE
- `make figures`: save plots (histogram + calibration)
- `make clean`: remove generated results and the audit log in `../artifact/`

## Docker
Run from the repository root:

```bash
docker build -t climate-radar -f code/docker/Dockerfile .
docker run --rm -v $PWD:/app climate-radar
```

## Contributing
- Keep modules small and pure (numpy/pandas/matplotlib only).
- No network calls; offline determinism.
- Seed any randomized component.
- `make reproduce` must pass locally.
