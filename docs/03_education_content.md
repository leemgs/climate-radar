# 교육 내용 (Training / Educational Content)

## 1. 실험 전 교육(Training) 개요

- 참가자는 본 실험 전에 **짧은 교육 세션**을 받음.
- 목표: 고위험 의사결정의 본질적 특성(변화하는 정보, 불확실성, 비대칭 오류 비용)을 이해하고, **적절한 행동 선택**에 집중하도록 유도.
- 도메인 전문 지식은 요구되지 않음 (참가자 중 고경험자는 0명).

### 지시사항 핵심

> “Participants were instructed to focus on taking the appropriate action rather than on analyzing the information.”

즉, 정보 분석보다 **행동 실행**에 초점을 맞추도록 교육됨.

---

## 2. 교육 내용

### 2.1 시스템 소개
- Climate RADAR / ACHDF의 목적: 재난 경보를 **적시 보호 행동**으로 전환하는 Human–AI 의사결정 지원
- 두 가지 인터페이스 조건 소개 (Baseline vs AI-assisted)
- AI 추천은 **보조**이며, 최종 결정은 항상 인간이 함

### 2.2 행동 옵션 설명
| 옵션 | 의미 | 사용 시점 예시 |
|------|------|----------------|
| Monitor | 지속 관찰 | 위험이 낮고 추가 정보 필요 시 |
| Standby | 준비 태세 | 위험이 상승 중이나 아직 행동 시점이 아닐 때 |
| Issue alert | 경보 발령 | 주민에게 주의를 환기해야 할 때 |
| Shelter in place | 실내 대피 | 즉시 이동이 어렵거나 위험할 때 |
| Recommend evacuation | 대피 권고 | 위험이 높고 대피가 필요할 때 |

### 2.3 AI-assisted 조건 추가 교육
- 불확실성 표시기 의미
- Criticality cue 의미
- Recommend 모드 vs Escalate 모드 차이
- 추천을 따르지 않아도 되며, deferral(보류) 플래그를 사용할 수 있음
- 가드레일이 적용된 추천만 표시됨

### 2.4 평가 기준 안내
- 주요 성과 지표: **Action Execution Rate (AER)** = 정답 행동 선택 비율
- 응답 시간도 기록되나, 속도만으로 평가하지 않음
- 설문: NASA-TLX (workload), Trust, SUS (usability)

---

## 3. 교육 흐름

1. 시스템 목적 및 Human-in-the-loop 원칙 설명 (5분)
2. 5가지 행동 옵션 의미와 오류 비용 설명 (5분)
3. Baseline 인터페이스 데모 + 연습 1 trial
4. AI-assisted 인터페이스 데모 (recommend / escalate) + 연습 1 trial
5. 설문 도구(NASA-TLX, Trust, SUS) 안내
6. 본 실험 시작

> 참고: 문서에 시간이 명시된 것은 1·2단계(각 5분)뿐이다. 3~6단계의 소요 시간과 총 교육 시간은 기록되어 있지 않다. 연습은 Baseline과 AI-assisted 조건 각각 1 trial씩 수행했다.

작성일: 2026-11-16  
기반 자료: Climate RADAR 실험 교육 자료 및 THMS 원고 Methods 섹션
