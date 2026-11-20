# Raw-Log Re-analysis: Data Audit Notes (Check Before Submission)

On 2026-11-15, the files in `data/` (from the attached `evaluation_result_en.zip`) were re-analyzed with `analysis/analyze.py`. Every number in the paper comes from this script (`analysis/results.json`).

## 1. What agreed with the paper
- AER 0.62 → 0.81, latency 12.4 → 8.1 s, NASA-TLX 59.8 → 46.2, trust 3.40 → 4.20, SUS (as logged) 68.5 → 81.7.
- AER is reproduced exactly as the share of trials with selected action = reference action. The logs contain no time window.

## 2. What differed from the previous manuscript (and was corrected)
- SDs: TLX 11.5/9.3 (previously 10.9/9.6); SUS 10.5/8.6 (previously 11.2/9.4).
- Four NASA-TLX subscales and the three trust-item means disagreed with the old tables; they were replaced by the log values (Table IX).
- The old "appropriate deferral 0.21/0.47, inappropriate reliance 0.18/0.09" cannot be computed from the logs (no AI-recommendation or correctness field) and were removed. In the logs, deferral is 0.18 (non-escalated) and 0.47 (escalated).

## 3. Anomalies in the data itself (reviewers or a data audit may raise these)
1. **SUS.** `SUS_overall` is 2.8–4.7 points higher than the standard score of the ten items in every row (recomputed means 65.7/77.0). Item consistency is very low (α = .44–.49; published SUS data typically exceed .85).
2. **Trust items.** α = .61 / .46. The logged overall trust score equals the item mean in baseline records but is 0.017–0.023 higher in all 52 AI-assisted records (4.20 vs. 4.18); disclosed in §IV-D.
3. **Response time.** The SD of participants' mean latencies is only about 0.8 s, and the correlation between conditions is about zero (r = −.09). Real human data usually show large between-participant variation and a high correlation across conditions. This produces an extreme d_z = −3.6.
4. Between-condition correlations of TLX, SUS and trust are also near zero (r = −.02 to .15).
5. **Scenario IDs (S01–S10)** do not correspond to reference actions. For the same participant and the same ID, the reference action matched across the two conditions in 18% of pairs (about 20% expected by chance). "Identical scenarios in both conditions" cannot be verified from the logs.
6. The data README describes the files as data "corresponding to" the reported means, SDs and significance levels. The earlier package README stated that the raw logs no longer existed.

**Implication.** Patterns such as 3–4 are more typical of data generated or reconstructed to match summary statistics than of raw participant responses. The manuscript describes the files as anonymized study logs and discloses the anomalies as limitations (§VII-D), but **the author must personally confirm that these files are the original logs collected in the experiment** before submission. If they are reconstructed or simulated data, the manuscript must say so; submitting them otherwise would be research misconduct.

## 4. Items only the author can supply (do not fabricate)
- IRB/ethics review status (currently stated as "not reviewed"), interface screenshots and a worked scenario example, training content and pass criterion, trust-item wording, interview coding and quotes, the prototype's risk model, thresholds and guardrail rules, how the reference action was derived, and the time limit.

## 5. Additional checks (2026-11-15): SUS and response-time recording
- **The SUS discrepancy is a per-condition constant:** +2.8 in all 52 baseline records and +4.7 in all 52 AI records (stored total minus the standard recomputation). It is not random error. How the totals were obtained (survey tool, adjustment formula, manual entry) cannot be determined from the files and needs author confirmation.
- **Response time:** stored per trial at 0.1 s resolution. The timer start and stop points, and any processing before release, cannot be determined from the files.
- Both facts are stated in §IV-F as "not documented".
- Recording method as described by the author: automatic system logs; response time = difference between the stimulus-display and response-submission timestamps; online survey tool (Qualtrics); condition order managed by the experimenter. This is reflected in §IV-F as "according to the study procedure". **This does not explain the constant SUS offsets (+2.8/+4.7)**, which remain "not documented".
- Author confirmation: the SUS totals are Qualtrics export values. However, a different constant per condition is not explained by standard scoring or by a single coding scheme (a coding scheme does not vary by condition). Please compare against the Qualtrics survey's scoring settings and the original export file. §IV-F should be replaced once the comparison is available.

## 6. Provenance confirmation
- 2026-11-16: the author confirmed that the files in `data/` are the original data collected in the study. This confirmation concerns provenance only; the constant SUS offsets and the other anomalies in Section 3 remain undocumented and stay disclosed in §IV-F and §VII-D of the manuscript.
