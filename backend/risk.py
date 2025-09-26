import math, random
from typing import Dict, Tuple
from .models import RiskInput, RiskOutput

def _normalize(v: float, a: float, b: float) -> float:
    if b == a:
        return 0.0
    return max(0.0, min(1.0, (v - a) / (b - a)))

def base_score(inp: RiskInput) -> Tuple[float, Dict[str,float]]:
    # Simple normalized components
    hazard = 0.0
    if inp.hazard_type in ("rain","flood"):
        rain = _normalize(inp.rain_mm_per_hr, 0, 80)  # 0~80mm/h
        river = _normalize(inp.river_level_pct, 0, 100)
        hazard = 0.6*rain + 0.4*river
    elif inp.hazard_type == "heat":
        t = _normalize(inp.feels_like_c, 20, 40)
        hazard = t
    elif inp.hazard_type == "wind":
        hazard = _normalize(inp.wind_mps, 0, 25)
    else: # cold
        hazard = _normalize(0 - inp.temp_c, -5, 15)  # inversed for cold

    exposure = 0.2 + (0.6 if inp.lowland else 0.0)  # lowland increases exposure
    vulnerability = 0.2 + 0.8 * inp.vulnerable_fraction

    score = inp.calibration_k * hazard * (0.5*exposure + 0.5*vulnerability)
    score = max(0.0, min(1.0, score))

    details = {
        "hazard": hazard,
        "exposure": exposure,
        "vulnerability": vulnerability,
        "calibration_k": inp.calibration_k,
    }
    return score, details

def grade(score: float) -> str:
    if score < 0.25: return "Low"
    if score < 0.5: return "Moderate"
    if score < 0.75: return "High"
    return "Severe"

def compute_with_uncertainty(inp: RiskInput) -> RiskOutput:
    random.seed(42)
    samples = []
    for _ in range(inp.mc_trials):
        # Perturb a few key inputs multiplicatively
        def jitter(x: float) -> float:
            sigma = inp.uncertainty_sigma
            return x * max(0.0, random.gauss(1.0, sigma))
        pert = inp.model_copy()
        pert.rain_mm_per_hr = jitter(inp.rain_mm_per_hr)
        pert.river_level_pct = jitter(inp.river_level_pct)
        pert.feels_like_c = jitter(inp.feels_like_c)
        pert.wind_mps = jitter(inp.wind_mps)
        pert.vulnerable_fraction = min(1.0, max(0.0, jitter(inp.vulnerable_fraction)))
        s, _ = base_score(pert)
        samples.append(s)

    samples.sort()
    mean = sum(samples)/len(samples)
    p05 = samples[int(0.05*len(samples))]
    p95 = samples[int(0.95*len(samples))-1]
    base, details = base_score(inp)

    return RiskOutput(
        risk_score=base,
        risk_grade=grade(base),
        mean=mean,
        p05=p05,
        p95=p95,
        details=details
    )
