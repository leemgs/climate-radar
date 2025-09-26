from typing import List
from .models import ActionInput, PersonaAction

def _t(language: str, ko: str, en: str) -> str:
    return ko if language == "ko" else en

def _template(hazard: str, grade: str, persona: str, language: str) -> str:
    if hazard in ("rain","flood"):
        if grade in ("High","Severe"):
            if persona == "citizen":
                return _t(language,
                    "지하 공간 출입을 즉시 중지하고 차량을 고지대로 이동하세요.",
                    "Avoid basements immediately and move vehicles to higher ground."
                )
            if persona == "senior":
                return _t(language,
                    "실내에 머무르며 젖은 바닥을 피하세요. 보호자에게 연락해 안전을 확인하세요.",
                    "Stay indoors, avoid wet floors, and contact a caregiver to confirm safety."
                )
            if persona == "volunteer":
                return _t(language,
                    "저지대 고립 가능 구역을 우선 순찰하고, 전력·통신 위험 구간을 우회하세요.",
                    "Patrol low-lying isolation zones first and avoid power/telecom risk areas."
                )
            if persona == "municipality":
                return _t(language,
                    "침수 예상 구역에 통제선을 설치하고, 취약가구 대상 안부 콜을 즉시 시작하세요.",
                    "Deploy cordons in forecast inundation areas and start welfare checks for vulnerable households."
                )
        else:
            return _t(language,
                "배수구를 점검하고, 하천·지하주차장 접근을 자제하세요.",
                "Check drains and avoid rivers/underground parking."
            )
    if hazard == "heat":
        if grade in ("High","Severe"):
            if persona in ("citizen","senior"):
                return _t(language,
                    "1시간 이내 냉방쉼터를 방문하고 수분을 충분히 섭취하세요.",
                    "Visit a cooling center within an hour and hydrate frequently."
                )
        return _t(language,
            "실외 활동을 줄이고 그늘에서 쉬세요.",
            "Reduce outdoor activity and rest in shade."
        )
    if hazard == "wind":
        return _t(language,
            "간판·낙하물에 주의하고 외출을 최소화하세요.",
            "Beware of falling objects and minimize travel."
        )
    # default
    return _t(language, "기본 안전 수칙을 따르세요.", "Follow standard safety precautions.")

def recommend(inp: ActionInput) -> List[PersonaAction]:
    out: List[PersonaAction] = []
    for p in inp.personas:
        g = _template(inp.hazard_type, inp.risk_grade, p, inp.language)
        rationale = _t(inp.language,
            f"{inp.hazard_type} 위험 {inp.risk_grade} 등급에 따른 표준 권고입니다.",
            f"Standard guidance for {inp.hazard_type} hazard at {inp.risk_grade} grade."
        )
        out.append(PersonaAction(
            persona=p,
            language=inp.language,
            guidance=g,
            rationale=rationale,
            confidence=0.75 if inp.risk_grade in ('High','Severe') else 0.6
        ))
    return out

def render_prompt(context: dict) -> str:
    # Example prompt for external LLMs
    return f"""You are a disaster guidance generator.
Inputs: {context}
Task: Produce 2-3 concise guidance sentences per persona (citizen, senior, volunteer, municipality), with rationale and confidence, in the requested language.
Constraints: Plain language, actionable verbs, avoid panic.
"""

def llm_generate(context: dict) -> dict:
    # Stub: replace with your model endpoint call
    prompt = render_prompt(context)
    return {"prompt": prompt, "output": None}
