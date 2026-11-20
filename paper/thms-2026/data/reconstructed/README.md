# Materials recovered from backup storage (post hoc reconstruction)

**Status.** The author states (2026-11-20) that these files were **re-created or re-organized from backup storage**. They are *not* original session output and are *not* the primary study data (those are `../01_*.csv`–`../03_*.csv`). Cite them only as "post hoc reconstruction".

**Reconciliation with the primary logs** (`../../analysis/reconcile_reconstructed.py`, `../../notes/reconstructed_reconciliation.md`): aggregate AER is similar (0.815 vs 0.810), but at trial level the recovered log agrees with the primary log on the selected action in only 22% of trials (chance ≈ 20%), and on escalation in 57%; it has 208 escalated trials against 150 in the primary log. The primary log therefore cannot be linked to this material, and **no result in the manuscript is computed from it**.

| File | What it is | How it is used |
|---|---|---|
| `scenario_config_and_design.xlsx` | Thresholds (τu 0.25, τc 0.70, τr 0.60) and a 10-scenario design table | Supplementary S8 (as reconstructed design; the 208 vs. 150 escalation conflict is disclosed) |
| `expert_consensus_reference_actions.xlsx` | Four-expert rating table for the reference actions | Supplementary S8 (as recovered; its "92%" statement does not match its table: 5/10 unanimous) |
| `training_checklist_and_records.xlsx` | Training protocol, pass criterion and 52 completion records | Supplementary S8 (its stated mean 18.4 min / 8 extra explanations do not match its rows: 19.6 min / 6) |
| `Fig_S1_Baseline.png`, `Fig_S2_Recommend.png`, `Fig_S3_Escalate.png` | Interface images | Supplementary S8 as **illustrative reconstructions**, not original screenshots (dates 2025 vs. 2024; risk shown as 0.71 and as 72) |
| `ai_recommendation_generation_log.csv` | 520 trial rows with AI recommendation and correctness | Not used for any reported number |
| `automation_bias_analysis_summary.md` | 41.3% (43/104) bias rate computed from the log above | **Not reported**: it is not evidence about the study because the log does not match the primary data |

The earlier statement in this folder that all materials are "consistent with the reported results" was not correct and has been removed.
