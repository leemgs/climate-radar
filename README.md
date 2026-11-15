# Climate RADAR

<p align="center">
  <img src="artifact/climate-radar-logo.png" alt="Climate RADAR Logo" width="150" height="150">
</p>

**Climate RADAR** (*Risk-Aware, Dynamic, and Action-Recommendation system*) studies how human–AI decision support can turn disaster alerts into timely protective actions. The project combines uncertainty-aware risk estimation, guardrailed AI recommendations, and human-in-the-loop escalation, and evaluates decision support by the actions people take rather than by prediction accuracy alone.

This repository contains the papers and a reproducible reference implementation.

## Repository layout

| Folder | Content |
|---|---|
| [`paper/`](./paper/) | Manuscripts, one folder per paper: [`thms-2026/`](./paper/thms-2026/) (IEEE THMS resubmission) and [`ijdrs-2025/`](./paper/ijdrs-2025/) (IJDRS submission) |
| [`code/`](./code/) | Reference implementation (synthetic data, risk model, guardrails, orchestration, fairness audit) with `make reproduce` and Docker |
| [`artifact/`](./artifact/) | Generated results and audit logs, model card, and project assets |

```
climate-radar/
├── paper/       # papers (LaTeX sources, submission PDFs, letters)
├── code/        # runnable implementation
├── artifact/    # generated outputs and assets
├── README.md, LICENSE, CITATION.cff, CONTRIBUTING.md, CODE_OF_CONDUCT.md
```

## Quickstart (reference implementation)

```bash
cd code
pip install -r requirements.txt
make reproduce          # outputs go to ../artifact/
```

See [`code/README.md`](./code/README.md) for details. The implementation uses synthetic data and is an educational reference, not for real-world emergency use.

## Papers

- **IEEE Transactions on Human-Machine Systems (resubmission in preparation):** *From Alerts to Actions: An Action-Centered Human–AI Decision Support Framework for Disaster Response.* See [`paper/thms-2026/`](./paper/thms-2026/).
- **International Journal of Disaster Risk Science (under review):** *From Alerts to Actions: Climate RADAR as a Generative AI–Driven Reliability Layer for Disaster Resilience.* See [`paper/ijdrs-2025/`](./paper/ijdrs-2025/).

## License
Apache License 2.0. See [`LICENSE`](./LICENSE).
