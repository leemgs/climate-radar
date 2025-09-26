# 🌦️ Climate RADAR — Hyperlocal Climate Response Platform

Climate RADAR is a generative‑AI platform that turns **alerts into actions** by producing hyperlocal, personalized guidance for citizens, volunteers, and municipal operators.

> This implementation traces directly to the submitted idea proposal (Korean) and its scope: risk‑index summarization, AI action‑card generation, check‑in/help requests, volunteer triage, and an institutional dashboard. See the original specification for user stories and KPIs. 

## ✨ Core Modules
- **Citizen app**: AI‑generated action cards (reason + confidence), easy‑Korean/multilingual.
- **Volunteer**: 3‑line AI summaries for nearby help requests.
- **Institution dashboard**: risk summary & request backlog report, heatmap data.
- **Conversational bot**: “What should I do now?” style Q&A.

## 🧱 Tech Stack
- **Backend**: FastAPI, SQLAlchemy (SQLite by default), Pydantic; optional OpenAI for LLM.
- **Frontend**:
  - `frontend/mobile_app`: minimal Expo (React Native) prototype screens.
  - `frontend/dashboard`: Vite + React dashboard starter.
- **AI Services**: pluggable LLM service; ships with a **mock** (deterministic) for offline use.

## 🚀 Quickstart
```bash
git clone https://github.com/your-username/climate-radar.git
cd climate-radar
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r backend/requirements.txt
cp backend/.env.example backend/.env                # fill values as needed
uvicorn backend.app:app --reload
```

Open:
- API docs: http://127.0.0.1:8000/docs
- Dashboard (dev): see `frontend/dashboard/README.md`
- Mobile app (Expo): see `frontend/mobile_app/README.md`

## 🔐 Environment
`backend/.env`:
```
OPENAI_API_KEY=
LLM_PROVIDER=mock   # mock | openai
DATABASE_URL=sqlite:///./climate.db
```

## 📦 API Overview
- `POST /api/recommendation` – AI action cards (citizen).
- `POST /api/checkin` – citizen safe/help check‑in.
- `POST /api/request_help` – create help request.
- `GET  /api/requests/nearby` – volunteer: unassigned nearby requests.
- `POST /api/requests/assign` – assign a request to a volunteer.
- `GET  /api/dashboard/summary` – high‑level summary for municipalities.
- `GET  /api/dashboard/heatmap_data` – risk tiles for heatmap.

Detailed contracts: **docs/API.md**.

## 📐 Architecture
See **docs/ARCHITECTURE.md** for data model, flow, and HITL hooks.

## 📝 License
Apache‑2.0 (see `LICENSE.md`).
