import os
from typing import Tuple

def _mock_llm(vulnerability: str, weather: dict) -> Tuple[str, str, float]:
    rainfall = weather.get("rainfall_mm_h") or weather.get("rainfall") or "N/A"
    river = weather.get("river_level_pct") or weather.get("river_level") or "N/A"
    temp = weather.get("temperature") or "N/A"
    if vulnerability in ["elderly", "고령자"]:
        text = "집에 머무르시고 미끄러운 바닥을 피하세요. 보호자나 이웃에게 전화로 안부를 알리세요."
        reason = f"강수 {rainfall}, 하천수위 {river}. 고령자 보호 우선."
        conf = 0.78
    elif vulnerability in ["with_children", "어린이 동반"]:
        text = "1시간 이내 가까운 냉방쉼터를 방문하고, 물을 충분히 섭취하세요. 야외 활동은 피하세요."
        reason = f"기온 {temp}. 어린이는 더위 취약."
        conf = 0.74
    else:
        text = "지하 공간 출입을 중지하고 차량을 고지대로 이동하세요."
        reason = f"강수 {rainfall}, 하천수위 {river}. 침수 위험."
        conf = 0.81
    return text, reason, conf

def generate_action_recommendation(vulnerability: str, weather: dict) -> Tuple[str, str, float]:
    provider = os.getenv("LLM_PROVIDER", "mock").lower()
    if provider == "mock" or not os.getenv("OPENAI_API_KEY"):
        return _mock_llm(vulnerability, weather)
    # Placeholder for real OpenAI call if configured (kept simple to avoid external dependency here).
    # In real usage, plug your OpenAI client here.
    return _mock_llm(vulnerability, weather)
