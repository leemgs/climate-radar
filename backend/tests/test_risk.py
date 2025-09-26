import math
from backend.models import RiskInput
from backend.risk import base_score, grade, compute_with_uncertainty

def test_risk_monotonicity():
    inp = RiskInput(hazard_type="flood", rain_mm_per_hr=0, river_level_pct=0, lowland=False, vulnerable_fraction=0.0)
    s0, _ = base_score(inp)
    inp.rain_mm_per_hr = 60
    inp.river_level_pct = 90
    s1, _ = base_score(inp)
    assert s1 > s0

def test_uncertainty_bounds():
    inp = RiskInput(hazard_type="heat", feels_like_c=39, vulnerable_fraction=0.3)
    out = compute_with_uncertainty(inp)
    assert 0 <= out.p05 <= out.mean <= out.p95 <= 1.0
    assert grade(out.risk_score) in ("Low","Moderate","High","Severe")
