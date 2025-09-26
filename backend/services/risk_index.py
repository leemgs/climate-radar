from typing import Dict
def compute_simple_risk(weather: Dict) -> float:
    """Return a naive risk score 0..1 from weather dict (demo only)."""
    score = 0.0
    if weather.get("rainfall_mm_h", 0) or weather.get("rainfall", 0):
        score += min(float(weather.get("rainfall_mm_h", weather.get("rainfall", 0))) / 100.0, 0.6)
    if weather.get("river_level_pct", 0) or weather.get("river_level", 0):
        score += min(float(weather.get("river_level_pct", weather.get("river_level", 0))) / 100.0, 0.3)
    if weather.get("temperature", 0) and float(weather["temperature"]) >= 35:
        score += 0.2
    return min(score, 1.0)
