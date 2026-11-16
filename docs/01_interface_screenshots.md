# 인터페이스 스크린샷 문서 (Interface Screenshots)

## 1. 연구 조건별 인터페이스 개요

연구에는 두 가지 조건이 사용되었습니다 (within-subjects, counterbalanced).

| 요소 | Baseline (기존 대시보드) | AI-assisted (ACHDF 기반) |
|------|--------------------------|---------------------------|
| 위험·재해 정보 | ✓ | ✓ |
| 명시적 불확실성 표시 | ✗ | ✓ |
| 중요도(Criticality) 큐 | ✗ | ✓ |
| 가드레일 검증된 행동 추천 | ✗ | ✓ (recommend 모드) |
| 에스컬레이션 프롬프트 (근거 + 선택지) | ✗ | ✓ (escalate 모드) |
| 최종 결정·실행 주체 | 인간 | 인간 |

- AI-assisted 조건에서 전체 520 trials 중 150 trials (28.8%)가 escalate 모드로 전환됨.

---

## 2. Baseline 인터페이스 구성

- **레이아웃**: 전통적인 재난 대시보드 형태
  - 상단: 위험 수준 요약 (수치/색상 코딩)
  - 중앙: 지도 또는 시계열 위험 지표
  - 하단/측면: 5가지 응답 옵션 버튼
    1. Monitor (모니터링)
    2. Standby (대기)
    3. Issue alert (경보 발령)
    4. Shelter in place (실내 대피)
    5. Recommend evacuation (대피 권고)
- 불확실성·중요도·추천 문구는 제공되지 않음.
- 사용자가 스스로 정보를 해석하고 행동을 선택.

---

## 3. AI-assisted (ACHDF) 인터페이스 구성

### 3.1 Recommend 모드
- 위험 점수 + 불확실성 표시기 (신뢰구간 또는 variance proxy)
- Criticality cue (중요도 배지)
- **가드레일 통과 추천 문구** (단일 행동 추천 + 짧은 근거)
- 5가지 행동 옵션은 여전히 선택 가능 (추천을 무시할 수 있음)
- 추천 예시 형태:
  - High risk: “IMMEDIATE: Move to nearest shelter; bring ID, water, and phone.”
  - Medium: “PREPARE: Pack essentials, confirm route to shelter, check on neighbors.”
  - Low: “STAY ALERT: Monitor updates; avoid low-lying areas.”
  - 하위 그룹(elderly/migrant)에 따른 추가 문장 포함

### 3.2 Escalate 모드
- 단일 추천 대신 **근거와 선택지**를 제시
- “이 케이스는 불확실성/중요도/정책 위반으로 인해 인간 검토가 필요합니다” 형태의 프롬프트
- 사용자가 직접 검토 후 행동 선택 또는 deferral 플래그 설정 가능

---

## 4. 공통 UI 요소

- 위험 점수(risk_score)와 분산(risk_var) 표시
- 응답 시간 측정: 화면 제시 시점 ~ 응답 제출 타임스탬프 차이
- Deferral 플래그 지원 (추가 확인이 필요하다고 표시)
- 에스컬레이션 플래그 자동 기록

---

## 5. 관련 코드 위치

- `code/src/llm/recommender.py` : 추천 문구 생성
- `code/src/llm/guardrails.py` : 텍스트 정제 및 용어 확장
- `code/src/orchestration/` : 실행 및 안전 예산
- `code/configs/policy.yaml`, `thresholds.yaml` : 정책·임계값

작성일: 2026-11-16  
기반 자료: Climate RADAR 실험 프로토타입 및 THMS 원고 Methods 섹션
