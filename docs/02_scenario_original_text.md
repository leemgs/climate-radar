# 시나리오 원문 (Scenario Original Text)

## 1. 실험 설계 요약

- 참가자당 조건별 10 trials (총 20 trials)
- 시나리오 라벨: **S01 ~ S10**
- 각 trial에서 참가자는 진화하는 위험에 대한 정보를 해석하고 다음 5가지 중 하나를 선택:
  1. **Monitor** (모니터링)
  2. **Standby** (대기)
  3. **Issue alert** (경보 발령)
  4. **Shelter in place** (실내 대피)
  5. **Recommend evacuation** (대피 권고)
- 정답 행동(reference/correct_action)은 로그에 기록됨.
- 작업 특성: 변화하는 정보, 불확실성, 비대칭 오류 비용(고위험 의사결정 특성 재현)

---

## 2. 시나리오 공통 구조

각 시나리오는 다음과 같은 정보 블록으로 구성되었습니다.

```
[시나리오 ID: S0X]
현재 시각: T
지역: [합성 지역명]
위험 요인:
  - Hazard (재해 강도)
  - Exposure (노출 정도)
  - Vulnerability (취약성)  ※ 모델에서 1-V로 반전
  - Social (사회적 요인)

현재 위험 점수(risk_score): [0–1]
불확실성(risk_var / uncertainty): [값]
하위 그룹 정보: baseline / elderly / migrant 등

상황 설명:
“[지역]에서 [재해 유형]이 진행 중입니다. 
최근 [N]시간 동안 지표가 [변화]하고 있으며, 
취약 계층에 대한 영향이 [수준]입니다.”
```

---

## 3. 시나리오별 원문

### S01 – 저위험 모니터링 상황
- 위험 수준: Low (risk ≈ 0.2)
- 정답: Monitor
- 설명: “강수량이 증가하고 있으나 아직 저지대 침수 위험은 낮습니다. 추가 관측이 필요합니다.”

### S02 – 중간 위험 준비 상황
- 위험 수준: Medium (risk ≈ 0.5)
- 정답: Standby 또는 Issue alert
- 설명: “하천 수위가 빠르게 상승 중입니다. 주민들에게 준비를 권고할 시점입니다.”

### S03 – 고위험 즉시 행동
- 위험 수준: High (risk ≥ 0.8)
- 정답: Shelter in place 또는 Recommend evacuation
- 설명: “돌발 홍수 위험이 임박했습니다. 즉시 대피 또는 실내 대피가 필요합니다.”

### S04–S10
- 위와 동일한 패턴으로 위험 수준·취약성·하위 그룹을 조합하여 변화시킴.
- S04–S10의 개별 원문은 이 문서에 수록되어 있지 않음.
- 일부 시나리오에서는 불확실성이 높아 escalate 모드가 트리거되도록 설계됨.

### 참고: 시나리오 정답 행동과 코드 추천의 관계
- 실험의 정답 행동(5개 옵션: Monitor/Standby/Issue alert/Shelter in place/Recommend evacuation)과 코드의 3단계 추천(STAY ALERT/PREPARE/IMMEDIATE)은 별개의 체계이다.
- 예: S02(risk ≈ 0.5)는 코드 임계값(0.6) 미만이라 STAY ALERT 구간이지만, 실험 정답 행동은 Standby 또는 Issue alert이다.

---

## 4. 로그에 기록된 필드

`03_trial_logs.csv` 기준:
- `scenario` : S01–S10
- `selected_action` : 참가자가 선택한 행동
- `correct_action` : 채점용 정답 행동
- `response_time_sec`
- `escalation` (0/1)
- `deferral` (0/1)

---

## 5. 논문 인용

> “In each trial, participants interpreted risk information about an evolving hazard and selected one of five response options: monitor, standby, issue alert, shelter in place, or recommend evacuation. The reference (correct) action of each trial is recorded in the log.”

작성일: 2026-11-16  
기반 자료: Climate RADAR 실험 시나리오 및 THMS 원고
