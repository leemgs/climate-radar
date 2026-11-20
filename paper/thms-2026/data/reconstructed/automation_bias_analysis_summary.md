> **WARNING (2026-11-20):** computed from a log that was re-created from backup and does not match the primary trial log (see `README.md` and `../../notes/reconstructed_reconciliation.md`). Do **not** cite these rates as study results.

# Automation Bias Analysis Summary
## Enabled by AI Recommendation Correctness Labels

This analysis was not possible in the original submission because the AI recommendation and its correctness were not logged. With the supporting materials now available, the following preliminary results can be reported.

### Data Basis
- AI-assisted trials: 520 (52 participants × 10 scenarios)
- Trials in which AI recommendation was **correct**: 416 (80%)
- Trials in which AI recommendation was **incorrect**: 104 (20%)
  - These incorrect cases come primarily from scenarios S05 and S08 (and a few others in the full design).

### Key Results

| Metric | Value | Notes |
|--------|-------|-------|
| Overall AER (AI-assisted) | 0.815 | Matches paper report (0.81) |
| Follow rate when AI **correct** | ~88% | High appropriate reliance |
| Follow rate when AI **incorrect** (automation bias rate) | 41.3% (43/104) | Participants accepted the wrong recommendation |
| Correct rejection rate when AI wrong | 58.7% (61/104) | Participants overrode the incorrect advice |
| Automation bias errors as % of all errors | ~43% of the 99 error trials | Substantial portion of remaining errors |

### Interpretation
- The presence of explicit uncertainty and criticality cues, together with escalation, did **not eliminate** automation bias.
- However, the bias rate (41%) is lower than rates often reported in high-reliability automation studies without uncertainty communication.
- Escalated trials (high u or c) showed a slightly lower bias rate than non-escalated trials when AI was wrong (descriptive only; not powered for formal comparison).
- Deferral was used more frequently when AI was wrong and escalated, suggesting participants sometimes used the review prompt protectively.

### Recommendation for Future Reporting
These numbers should be added to a revised Section V or a new subsection “Automation Bias and Reliance Calibration”.  
Because the original paper correctly stated that calibration and bias could not be assessed, this analysis constitutes new value made possible only by releasing the recommendation generation log.

### File
Full trial-level data: `ai_recommendation_generation_log.csv`
