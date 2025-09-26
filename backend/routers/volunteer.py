from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..db import get_db
from .. import models, schemas
from math import hypot

router = APIRouter(prefix="/api/requests", tags=["volunteer"])

@router.get("/nearby", response_model=list[schemas.HelpRequestOut])
def nearby(latitude: float = Query(...), longitude: float = Query(...), db: Session = Depends(get_db)):
    # naive distance filter on unassigned
    rows = db.query(models.HelpRequest).filter(models.HelpRequest.status=="unassigned").limit(100).all()
    def dist(r): return hypot(r.latitude - latitude, r.longitude - longitude)
    rows.sort(key=dist)
    return [
        schemas.HelpRequestOut(id=r.id, request_type=r.request_type, description=r.description,
                               latitude=r.latitude, longitude=r.longitude, status=r.status)
        for r in rows[:20]
    ]

@router.post("/assign")
def assign(payload: schemas.HelpRequestAssignIn, db: Session = Depends(get_db)):
    req = db.get(models.HelpRequest, payload.request_id)
    vol = db.get(models.User, payload.volunteer_id)
    if not req or not vol:
        raise HTTPException(status_code=404, detail="request or volunteer not found")
    req.assigned_volunteer_id = vol.id
    req.status = "assigned"
    db.commit()
    return {"ok": True}
