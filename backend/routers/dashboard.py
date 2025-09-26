from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .. import models, schemas
from ..services.risk_index import compute_simple_risk

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])

@router.get("/summary", response_model=schemas.SummaryOut)
def summary(db: Session = Depends(get_db)):
    unassigned = db.query(models.HelpRequest).filter(models.HelpRequest.status=="unassigned").count()
    assigned = db.query(models.HelpRequest).filter(models.HelpRequest.status=="assigned").count()
    resolved = db.query(models.HelpRequest).filter(models.HelpRequest.status=="resolved").count()
    return {"high_risk_areas": ["A-동", "B-동"], "unassigned_count": unassigned, "assigned_count": assigned, "resolved_count": resolved}

@router.get("/heatmap_data", response_model=schemas.HeatmapOut)
def heatmap(db: Session = Depends(get_db)):
    # demo tiles synthesized from recent weather rows
    tiles = []
    for w in db.query(models.WeatherDatum).order_by(models.WeatherDatum.id.desc()).limit(50).all():
        risk = compute_simple_risk({"rainfall_mm_h": w.rainfall_mm_h, "river_level_pct": w.river_level_pct, "temperature": w.temperature})
        tiles.append({"lat": w.latitude, "lon": w.longitude, "risk": float(risk)})
    return {"tiles": tiles}
