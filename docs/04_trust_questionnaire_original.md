# 신뢰 문항 원문 (Trust Questionnaire Original Text)

## 1. 신뢰 척도 개요

- 측정 시점: 각 조건(Baseline / AI-assisted) 종료 후
- 척도: 1–5 Likert (정수)
- 구성: **Overall Trust** + **3개 하위 문항**
  - `trust_reliability`
  - `trust_predictability`
  - `trust_appropriateness`
- 논문 보고 결과:
  - Baseline Overall: 3.4
  - AI-assisted Overall: 4.2
- Cronbach’s α: Baseline ≈ 0.61, AI ≈ 0.46

---

## 2. 문항 원문

| 필드명 | 문항 (영어) | 문항 (한국어) |
|--------|------------------|--------------------|
| trust_reliability | I can rely on the system’s recommendations when making decisions. | 의사결정을 할 때 이 시스템의 추천을 신뢰할 수 있다. |
| trust_predictability | The system’s behavior is predictable. | 이 시스템의 동작은 예측 가능하다. |
| trust_appropriateness | The system’s recommendations are appropriate for the situation. | 이 시스템의 추천은 상황에 적합하다. |
| Trust Overall | (3문항 평균인지 별도 문항인지 문서상 확정되지 않음) | 전반적으로 이 시스템을 신뢰한다. |

---

## 3. 관련 다른 설문

### NASA-TLX (Workload)
- 6개 하위 척도: Mental Demand, Physical Demand, Temporal Demand, Performance, Effort, Frustration
- Overall = 6개 하위척도 평균
- 보고값: Baseline 59.8 → AI 46.2

### SUS (System Usability Scale)
- 표준 10문항 (1–5 Likert)
- 로그의 `SUS_overall`은 표준 채점 결과와 정확히 일치하지 않음 (조건별 상수 보정 존재: +2.8 / +4.7)
- 보고값: Baseline 68.5 → AI 81.7
- 표준 재계산 시 약 65.7 / 77.0

---

## 4. 데이터 위치

- `artifact/user-study/.../02_survey_scores.csv`
- `paper/thms-2026/data/02_survey_scores.csv`
- 컬럼: participant, condition, Trust Overall, trust_reliability, trust_predictability, trust_appropriateness, SUS 관련 컬럼, NASA-TLX 관련 컬럼

---

## 5. 참고사항

- Cronbach’s α가 낮아(Baseline ≈ 0.61, AI ≈ 0.46) 척도의 내적 일관성에 대한 해석에 주의가 필요함.
- Overall Trust가 3문항 평균인지 별도 문항인지는 이 문서만으로 확정할 수 없음. 원 데이터(`02_survey_scores.csv`) 확인 필요.
- 논문에서도 trust calibration이나 automation bias를 직접 평가하지 못했음을 한계로 명시.

작성일: 2026-11-16  
기반 자료: Climate RADAR 실험 설문 원문 및 THMS 원고 Results 섹션
