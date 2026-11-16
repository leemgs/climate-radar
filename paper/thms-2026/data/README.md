# Experiment Data

This folder contains the actual experiment logs reported in the paper. It provides the experimental data corresponding to the reported means, standard deviations, and significance levels. All data have been anonymized to protect participant privacy.

## File Structure

1. **01_participant_info.csv**
    - `participant`, `age`, `gender`, `tech_background`, `disaster_experience`, `condition_order`
    - n = 52, anonymized
2. **02_survey_scores.csv**
    - `participant` × `condition` (`Baseline` / `AI`)
    - NASA-TLX: Overall + 6 subscales (`mental_demand`, `physical_demand`, `temporal_demand`, `performance`, `effort`, `frustration`)
    - Trust: Overall + 3 items (`trust_reliability`, `trust_predictability`, `trust_appropriateness`)
    - SUS: Overall (0–100) + 10 items (`SUS_1` ~ `SUS_10`)
3. **03_trial_logs.csv** (Primary Dataset)
    - `participant`, `condition`, `condition_order`, `scenario`, `selected_action`, `correct_action`, `response_time_sec`, `escalation`, `deferral`
    - 52 participants × 2 conditions × 10 scenarios = 1,040 rows

## Key Statistics

| Metric | Baseline | AI-assisted | Reported in Paper |
| --- | --- | --- | --- |
| AER | 0.62 | 0.81 | 0.62 / 0.81 |
| Response Time (sec) | 12.4 | 8.1 | 12.4 / 8.1 |
| NASA-TLX Overall | 59.8 | 46.2 | 59.8 / 46.2 |
| Trust Overall | 3.4 | 4.2 | 3.4 / 4.2 |
| SUS | 68.5 | 81.7 | 68.5 / 81.7 |

## Notes on Scales
- SUS items and Trust items are recorded as integers on a 1–5 Likert scale, consistent with the original instruments.
- NASA-TLX overall is the mean of the six subscales.
- SUS overall is computed from the 10 items using the standard SUS scoring formula.

## Notice
- This dataset may not be used for commercial purposes and is strictly restricted to the reproduction of this study and analytical practice.

## Correction note (added 2026-11-16, paper revision)
- `SUS_overall` in `02_survey_scores.csv` is **not** the standard SUS score of the ten stored items: it is higher by exactly 2.8 points in all 52 Baseline rows and by exactly 4.7 points in all 52 AI rows (recomputed means 65.7 / 77.0). The stored values are the Qualtrics export values; the scoring configuration behind them is not documented. The paper reports both (Section IV-F, V-B).
- `correct_action` ("reference action") is the scoring key as recorded; how it was derived is not documented. Scenario labels S01–S10 do not map to a fixed reference action.
