from pydantic import BaseModel, Field
from typing import Optional, List

class Location(BaseModel):
    latitude: float
    longitude: float

class RecommendationIn(BaseModel):
    weather_data: dict
    location_data: Location
    vulnerability: str = Field(description="e.g., 'elderly', 'with_children', 'general'")

class RecommendationOut(BaseModel):
    recommendation: str
    reason: str
    confidence: float

class CheckIn(BaseModel):
    user_id: int
    status: str = Field(pattern="^(safe|help)$")
    location: Location

class HelpRequestIn(BaseModel):
    user_id: int
    request_type: str
    description: Optional[str] = None
    location: Location

class HelpRequestAssignIn(BaseModel):
    request_id: int
    volunteer_id: int

class HelpRequestOut(BaseModel):
    id: int
    request_type: str
    description: Optional[str] = None
    latitude: float
    longitude: float
    status: str

class SummaryOut(BaseModel):
    high_risk_areas: List[str]
    unassigned_count: int
    assigned_count: int
    resolved_count: int

class HeatTile(BaseModel):
    lat: float
    lon: float
    risk: float

class HeatmapOut(BaseModel):
    tiles: List[HeatTile]
