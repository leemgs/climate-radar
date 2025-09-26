from fastapi import APIRouter, Depends, HTTPException
from ..schemas import RecommendationIn, RecommendationOut
from ..services.llm import generate_action_recommendation
from ..services.risk_index import compute_simple_risk

router = APIRouter(prefix="/api", tags=["citizen"])

@router.post("/recommendation", response_model=RecommendationOut)
def recommendation(payload: RecommendationIn):
    if not payload.weather_data or not payload.location_data:
        raise HTTPException(status_code=400, detail="Missing weather or location data")
    rec, reason, conf = generate_action_recommendation(payload.vulnerability, payload.weather_data)
    # augment confidence from naive risk
    conf = float(min(1.0, max(conf, compute_simple_risk(payload.weather_data))))
    return {"recommendation": rec, "reason": reason, "confidence": conf}
