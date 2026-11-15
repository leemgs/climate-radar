# User-study data (THMS manuscript)

Anonymized records of the controlled user study reported in [`../../paper/thms-2026/`](../../paper/thms-2026/) (n = 52, 2 conditions × 10 trials).

| Path | Content |
|---|---|
| `evaluation_result_en_20261115_1700.zip` | Archive as received (2026-11-15 17:00) |
| `evaluation_result_en_20261115_1700/` | Its contents: `01_participant_info.csv`, `02_survey_scores.csv`, `03_trial_logs.csv`, `README.md` (file structure and scales) |

Recording method (as stated by the author): trial logs are recorded automatically by the system (selections, response time, escalation flag); response time is the difference between the stimulus-display and response-submission timestamps; questionnaires were collected with an online survey tool and stored as integer 1–5 Likert responses; participant information comes from a pre-study questionnaire, and the condition order was managed by the experimenter.

Use: restricted to reproducing this study and analytical practice; no commercial use. The analysis scripts are in [`../../paper/thms-2026/analysis/`](../../paper/thms-2026/analysis/); a working copy of the CSV files is in `paper/thms-2026/data/`.

Known data-consistency notes (SUS overall vs. items, latency variance, scenario labels) are in [`../../paper/thms-2026/notes/data_audit_ko.md`](../../paper/thms-2026/notes/data_audit_ko.md).
