from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .models import RiskInput, ActionInput, HelpRequest, Volunteer
from .risk import compute_with_uncertainty
from .actions import recommend, llm_generate
from . import db
from pathlib import Path

app = FastAPI(title="Climate RADAR Prototype", version="0.1.0")

origins = ["http://127.0.0.1:8000", "http://localhost:8000"]
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

# init DB
db.init()

# Static frontend
frontend_dir = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/", StaticFiles(directory=str(frontend_dir), html=True), name="frontend")

@app.post("/api/risk/compute")
def api_compute(inp: RiskInput):
    res = compute_with_uncertainty(inp)
    return JSONResponse(res.model_dump())

@app.post("/api/actions/recommend")
def api_actions(inp: ActionInput):
    return [a.model_dump() for a in recommend(inp)]

@app.post("/api/llm/prompt")
def api_llm(context: dict):
    return llm_generate(context)

@app.post("/api/requests")
def api_add_request(req: HelpRequest):
    rid = db.add_request(req.name, req.lat, req.lon, req.need, req.priority)
    return {"id": rid}

@app.get("/api/requests")
def api_list_requests():
    return db.list_requests()

@app.post("/api/volunteers")
def api_add_volunteer(vol: Volunteer):
    vid = db.add_volunteer(vol.name, vol.lat, vol.lon, vol.capability)
    return {"id": vid}

@app.get("/api/volunteers")
def api_list_volunteers():
    return db.list_volunteers()

@app.post("/api/assign")
def api_assign():
    return db.greedy_assign()
