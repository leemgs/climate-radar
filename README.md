# Climate RADAR – Risk‑Aware, Dynamic, Action‑Recommendation (Prototype)

> From alerts **to actions**: a minimal, reproducible prototype that computes a composite risk index with propagated uncertainty, generates **personalized action cards**, records *help* requests, and provides a lightweight dashboard for **citizens, volunteers, and municipalities**.

This codebase implements a functional slice of the system described in the attached concept/proposal document (“기후 레이다(Climate RADAR) — 생성형 AI 기반 하이퍼로컬 기후대응 플랫폼”).

## Features

- **Risk Index API** (`/api/risk/compute`): combines meteorological & exposure inputs; supports uncertainty via Monte‑Carlo.
- **Action Recommendation API** (`/api/actions/recommend`): rule‑based templates + promptable outputs; multilingual (ko/en).
- **Requests & Volunteers** (`/api/requests`, `/api/volunteers`): SQLite persistence and simple matching.
- **Static Dashboard**: single‑page UI to compute risk, view action cards, submit help, and assign volunteers.
- **Reproducibility**: deterministic seeds, sample fixtures under `data/`, and unit tests for core calculations.
- **Security-by-default**: CORS narrowed to localhost, input validation via Pydantic, basic rate‑limit hook (per‑IP bucket).

> This prototype purposefully avoids external model calls so it runs **offline**. To connect an LLM, implement the stub in `backend/actions.py`.

## Quickstart

### 1) Run locally (Python 3.10+)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.app:app --reload
```

Open `http://127.0.0.1:8000/` for the dashboard. Explore `http://127.0.0.1:8000/docs` for the OpenAPI spec.

### 2) Docker

```bash
docker compose -f docker/docker-compose.yml up --build
```

### 3) Seed sample data

```bash
python scripts/seed_db.py
```

## Project Layout

```
climate-radar/
├── backend/
│   ├── app.py               # FastAPI app, routes, static serving
│   ├── risk.py              # Composite risk & uncertainty
│   ├── actions.py           # Rule-based + promptable actions
│   ├── db.py                # SQLite schema + helpers
│   ├── models.py            # Pydantic models
│   ├── requirements.txt
│   └── tests/
│       └── test_risk.py
├── frontend/
│   ├── index.html           # Single-page dashboard
│   ├── app.js               # UI logic, fetch helpers
│   └── styles.css
├── data/
│   └── sample_inputs.json   # Example hazard/exposure inputs
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── scripts/
│   ├── run.sh
│   └── seed_db.py
├── LICENSE.md               # Apache-2.0
└── README.md
```

## API Overview

- `POST /api/risk/compute` → risk index with uncertainty
- `POST /api/actions/recommend` → action cards for personas
- `POST /api/requests` / `GET /api/requests` → citizen help requests
- `POST /api/volunteers` / `GET /api/volunteers` → volunteer registry
- `POST /api/assign` → greedy nearest-match assignment

See full schemas in `backend/models.py` and interactive docs at `/docs`.

## Method Summary

- **Risk index**: normalized hazard × exposure × vulnerability with optional calibration factor `k`. Uncertainty propagation via parametric perturbation (Gaussian) across `N` trials (default 500) → mean, CI, and a categorical risk grade.
- **Actions**: rule templates pivot on risk grade, hazard type, and persona; supports tone control and multilingual strings. A `render_prompt()` stub demonstrates how to pass richer context to an external LLM.

## Testing

```bash
pytest -q backend/tests/test_risk.py
```

## Extending

- Replace `actions.llm_generate()` with calls to your model endpoint.
- Swap SQLite for Postgres; add auth (JWT); plug in real sensors/feeds.
- Add localization files under `frontend/i18n/` and wire to UI.

## License

Apache-2.0. See `LICENSE.md`.
