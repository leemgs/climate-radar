# 위험모델 임계값 · 가드레일 규칙 (Risk Model Thresholds & Guardrail Rules)

## 1. 위험 임계값 (Risk Thresholds)

파일: `code/configs/thresholds.yaml`

```yaml
risk_thresholds:
  low: 0.3
  medium: 0.6
  high: 0.8
```

### 해석
| 구간 | 조건 | 추천 행동 (recommender.py) |
|------|------|-----------------------------|
| Low | risk < 0.3 | STAY ALERT: Monitor updates; avoid low-lying areas. |
| Medium | 0.3 ≤ risk < 0.6 | STAY ALERT (코드상 별도 분기 없음; 아래 정확한 분기 참조) |
| High | risk ≥ 0.8 | IMMEDIATE: Move to nearest shelter; bring ID, water, and phone. |
| Medium 이상 | risk ≥ 0.6 | PREPARE: Pack essentials, confirm route to shelter, check on neighbors. |

정확한 분기:
- `r >= high (0.8)` → IMMEDIATE
- `r >= medium (0.6)` → PREPARE
- 그 외 → STAY ALERT

> 코드 대조 확인(`code/src/llm/recommender.py`): 분기는 `high`(0.8)와 `medium`(0.6)만 사용한다. `low`(0.3)는 `thresholds.yaml`에 정의되어 있으나 저장소 전체 코드에서 참조되지 않는다(미사용). 따라서 risk < 0.6은 모두 STAY ALERT로 처리된다. `medium`은 추천 분기 외에 `pipeline.py`의 `cmd_eval`에서 AER/EOD 계산의 `thr`로도 사용된다.

---

## 2. 안전 예산 (Safety Budgets)

같은 파일:

```yaml
safety_budgets:
  message_blast_radius: 0.2   # share only to first 20% entities in a cycle
  rollback_window_minutes: 3
  max_alerts_per_hour_vulnerable: 2
```

- **message_blast_radius**: 한 사이클에서 전체 엔티티의 20%까지만 메시지 전파
- **rollback_window_minutes**: 3분 이내 롤백 가능 창
- **max_alerts_per_hour_vulnerable**: 취약 계층에 대한 시간당 최대 경보 수 2회

관련 코드: `code/src/orchestration/safety_budgets.py`

```python
def within_blast_radius(current_fraction: float, budget: float) -> bool:
    return current_fraction <= budget
```

---

## 3. 정책 (Policy) 및 가드레일

파일: `code/configs/policy.yaml`

```yaml
allow_terms:
  - evacuation
  - shelter
  - bottled water
  - cooling center

deny_terms:
  - medical diagnosis
  - evacuation by force

jargon_glossary:
  - term: "AER"
    plain: "Action Execution Rate (how often recommended actions are taken)"
  - term: "ECE"
    plain: "Expected Calibration Error (match between scores and outcomes)"

languages_supported: ["en", "ko"]
```

### 가드레일 함수 (`guardrails.py`)

1. **sanitize(text, deny_terms)**  
   - deny_terms에 포함된 단어가 있으면 `[REDACTED]`로 치환

2. **glossary_expand(text, glossary)**  
   - 전문 용어를 “용어 (쉬운 설명)” 형태로 확장

### 추천 생성 시 적용 순서 (`recommender.py`)

1. 위험 점수에 따라 기본 추천 문구 생성
2. 하위 그룹(elderly / migrant)에 따른 추가 문장 삽입
3. `glossary_expand` 적용
4. `sanitize` 적용 (deny_terms 필터링)

---

## 4. 위험 모델 자체 (Bayesian Linear)

파일: `code/src/model/risk_model.py`

- 입력 특징: `hazard`, `exposure`, `vulnerability`, `social`
- vulnerability는 `1 - vulnerability`로 반전
- 절편 포함 선형 모델
- 베이지안 사후분포:  
  `sigma2 = 0.10`, `tau2 = 2.0`
- 출력: `risk_score` (0–1 clip), `risk_var` (분산)

```python
def bayes_linear_posterior(X, y, sigma2=0.10, tau2=2.0) -> Posterior
def predict_posterior(X, post)
def fit_composite_risk(df)
```

---

## 5. 에스컬레이션 로직 (논문 Algorithm)

```
Require: risk estimate r, uncertainty u, action criticality c
Require: policy-violation flag v ∈ {0,1}
Require: thresholds τ_r, τ_u, τ_c

if u ≥ τ_u or c ≥ τ_c or v = 1:
    mode ← “escalate”   # 인간 검토로 라우팅
elif r ≥ τ_r:
    mode ← “recommend”  # 제한된 자율성
else:
    mode ← (저위험 처리)
```

참고 구현의 임계값(`0.3 / 0.6 / 0.8`)이 위 τ_r에 해당함. τ_u(불확실성)와 τ_c(행동 중요도)의 구체적 값은 이 문서에 명시되어 있지 않다. 코드 대조 결과, 이 에스컬레이션 알고리즘(escalate/recommend 모드 분기)은 저장소 코드(`code/`)에 구현되어 있지 않으며 설정 파일에도 τ_u, τ_c 항목이 없다. 즉 이 알고리즘은 논문 기술이며, `recommender.py`는 모드 구분 없이 risk_score만으로 추천을 생성한다.

---

## 6. 요약 표

| 항목 | 값 / 규칙 | 위치 |
|------|-----------|------|
| Low 임계값 | 0.3 | thresholds.yaml |
| Medium 임계값 | 0.6 | thresholds.yaml |
| High 임계값 | 0.8 | thresholds.yaml |
| Blast radius | 0.2 | thresholds.yaml |
| Rollback window | 3 min | thresholds.yaml |
| Max alerts (vulnerable) | 2 / hour | thresholds.yaml |
| Deny terms | medical diagnosis, evacuation by force | policy.yaml |
| Sanitize | deny_terms → [REDACTED] | guardrails.py |
| Glossary expand | AER, ECE 등 | guardrails.py + policy.yaml |

---

## 6-1. 코드 대조로 확인된 추가 사항

- `policy.yaml`의 `allow_terms`는 코드 어디에서도 사용되지 않는다(`deny_terms`와 `jargon_glossary`만 사용).
- `sanitize()`는 과거 검사는 대소문자 무시, 치환은 대소문자 구분이라 "Medical Diagnosis" 같은 표기가 치환되지 않는 버그가 있었다. 현재는 `re.sub(..., flags=re.IGNORECASE)`로 수정되어 대소문자와 무관하게 `[REDACTED]`로 치환된다.
- 추천 생성 순서는 문서 기술과 일치한다: 기본 문구 → 하위 그룹(elderly/migrant) 문장 → `glossary_expand` → `sanitize`.
- 블라스트 반경은 `pipeline.py`의 `cmd_recs`에서 `sent/n <= 0.2`로 검사하므로, 전체의 20%를 넘는 1건까지 발송될 수 있다(예: n=10이면 3건).

## 7. 주의사항

- 이 구현은 교육 및 논문 재현용이며, 실제 비상 상황 사용을 목적으로 하지 않음.

작성일: 2026-11-16  
기반 자료: Climate RADAR 실험 코드 및 설정 파일
