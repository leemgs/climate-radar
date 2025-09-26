# Architecture & Data Model

- DB: `users`, `requests`, `weather_data`
- Flow: data ingest → risk estimate → LLM action text → UI surfaces
- HITL: municipal operator can validate templates and thresholds (future work).

This prototype keeps the LLM behind a service (`services/llm.py`) with a **mock** provider by default.
Switch to a real provider by setting `LLM_PROVIDER=openai` and `OPENAI_API_KEY`.
