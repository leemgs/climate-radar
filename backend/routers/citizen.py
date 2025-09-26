from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .. import models, schemas

router = APIRouter(prefix="/api", tags=["citizen"])

@router.post("/checkin")
def checkin(payload: schemas.CheckIn, db: Session = Depends(get_db)):
    user = db.get(models.User, payload.user_id)
    if not user:
        user = models.User(id=payload.user_id, username=f"user{payload.user_id}", role="citizen")
        db.add(user)
    user.latitude = payload.location.latitude
    user.longitude = payload.location.longitude
    db.commit()
    return {"ok": True, "status": payload.status}

@router.post("/request_help", response_model=schemas.HelpRequestOut)
def request_help(payload: schemas.HelpRequestIn, db: Session = Depends(get_db)):
    req = models.HelpRequest(
        user_id=payload.user_id,
        request_type=payload.request_type,
        description=payload.description,
        latitude=payload.location.latitude,
        longitude=payload.location.longitude,
        status="unassigned"
    )
    db.add(req)
    db.commit()
    db.refresh(req)
    return schemas.HelpRequestOut(
        id=req.id, request_type=req.request_type, description=req.description,
        latitude=req.latitude, longitude=req.longitude, status=req.status
    )
