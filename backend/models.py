from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Dict

HazardType = Literal["rain", "flood", "heat", "cold", "wind"]

class RiskInput(BaseModel):
    hazard_type: HazardType = Field(..., description="Primary hazard type")
    rain_mm_per_hr: float = 0.0
    river_level_pct: float = 0.0
    temp_c: float = 20.0
    feels_like_c: float = 20.0
    wind_mps: float = 0.0
    lowland: bool = False
    vulnerable_fraction: float = Field(0.0, ge=0.0, le=1.0, description="Population fraction considered vulnerable")
    calibration_k: float = Field(1.0, gt=0.0, description="Calibration multiplier")
    # Uncertainty
    uncertainty_sigma: float = Field(0.05, ge=0.0, description="Relative sigma for perturbation")
    mc_trials: int = Field(500, ge=50, le=5000, description="Monte Carlo trials")

class RiskOutput(BaseModel):
    risk_score: float
    risk_grade: Literal["Low","Moderate","High","Severe"]
    mean: float
    p05: float
    p95: float
    details: Dict[str,float]

class PersonaAction(BaseModel):
    persona: Literal["citizen","senior","volunteer","municipality"]
    language: Literal["ko","en"] = "ko"
    guidance: str
    rationale: str
    confidence: float

class ActionInput(BaseModel):
    hazard_type: HazardType
    risk_grade: Literal["Low","Moderate","High","Severe"]
    personas: List[Literal["citizen","senior","volunteer","municipality"]] = ["citizen"]
    language: Literal["ko","en"] = "ko"
    context: Optional[Dict[str, str]] = None

class HelpRequest(BaseModel):
    id: Optional[int] = None
    name: str
    lat: float
    lon: float
    need: Literal["medical","water","evacuation","checkin"]
    priority: int = 2

class Volunteer(BaseModel):
    id: Optional[int] = None
    name: str
    lat: float
    lon: float
    capability: Literal["medical","logistics","rescue","general"]
