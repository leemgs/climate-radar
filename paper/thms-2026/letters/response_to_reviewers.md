# Response to Reviewers: THMS-26-02-0115 (Resubmission)

**Original manuscript:** "From Alerts to Actions: A Human–AI Decision System for Reliable Action Execution Under Disaster Risk," THMS-26-02-0115  
**Revised title:** "From Alerts to Actions: An Action-Centered Human–AI Decision Support Framework for Disaster Response" (the word "Reliable" was removed because reliability of action execution was not measured)  
**Decision letter:** 12-Nov-2026, Reject and Resubmit (Dr. L. Trajkovic, Editor-in-Chief)

## Files in this folder

Materials are organized under `paper/thms-2026/` (see `paper/thms-2026/README.md` for the full layout).

| Location | Content |
|---|---|
| `submission/` | **Files to upload:** manuscript PDF, marked-up diff PDF, cover letter PDF, response PDF (English) |
| `manuscript/main.tex` | Revised manuscript source (`main_original.tex`: previous submission) |
| `letters/` | Markdown sources of the cover letter and the response to reviewers (English only) |
| `notes/reviewer_risk_assessment.md` | Reviewer-perspective risk assessment |
| `Makefile` | `make` rebuilds the manuscript, diff, and letter PDFs |

> **Before resubmission:** no `\TODO` items remain in the manuscript, and the cover letter is dated. The author confirmed on 2026-11-16 that the records in `data/` are the original data collected in the study (see `notes/data_audit.md`).

## Summary of the revision

We thank the Editor-in-Chief, the Associate Editor, and the three reviewers for their careful and constructive evaluation. We have revised the manuscript substantially and respond to every comment below. The main changes are:

1. **Positioning.** Following Reviewer 3, the paper no longer presents action-centered evaluation as a new concept. ACHDF is presented as a domain-specific instantiation of the joint cognitive systems perspective and of adaptive function allocation for AI-generated recommendations in disaster response, with a new related-work subsection (§II-A) and the foundational literature cited.
2. **Constructs.** A new Table I defines the role and operational definition of uncertainty, criticality, guardrails, bounded autonomy, escalation, trust, workload, and action execution. The manuscript now states consistently that only the level and form of AI support varies; decision authority always remains with the human.
3. **Methods and statistics.** Hypotheses (H1 primary; H2–H4 secondary), the task, the two interfaces (Table II), all measures, and a complete analysis plan are reported. For every outcome we report means and SDs, the paired difference with its 95% CI, the paired t statistic, the Holm-adjusted p value, and d_z with its CI, together with assumption checks, a trial-level logistic model, a mixed model for latency, order and carry-over tests, and a power sensitivity analysis. These statistics were computed from the anonymized trial-level logs and questionnaire records, which are provided with the paper together with the analysis script.
4. **Action Execution Rate.** AER is defined from the logs (selected action equals reference action) and separated from timeliness: every unsuccessful trial was a wrong-action trial, and wrong and correct trials had the same latency (§V-A).
5. **Claims.** Claims about mechanism, trust calibration, automation bias, the benefit of the action format, and cross-domain generalizability were removed or reframed as hypotheses. Results now contain only findings; interpretation is in §VI.
6. **Length.** To meet the journal's 10-page limit for regular papers, the manuscript was shortened from 15 to 10 pages (including references). Nothing requested by the reviewers was removed. The tables of response-option meanings, measures, hypothetical time cutoffs, escalation status, qualitative themes, demographics, design implications, and cross-domain mapping, as well as two figures (conceptual layers and outcome summary), were converted into text or removed, and eight tangential references were dropped. The tables and figures cited in this letter use the new numbering.
7. **Transparency.** What the study records do not document is stated explicitly in §VII-D rather than omitted. Where recomputation changed values from the previous version, we list the changes below.

## Associate Editor

| AE concern | Response | Location |
|---|---|---|
| Difference from JCS and adaptive function allocation | Explicit positioning as an instantiation, plus a new related-work subsection | §I (end), §II-A, §III |
| Roles and implementation of uncertainty, criticality, guardrails, escalation, trust, workload, bounded autonomy | New construct table; "bounded autonomy" defined as bounded *generation* of recommendations; trust and workload declared design considerations and outcomes, not run-time states. Implementation details that cannot be reported are stated as such. | Table I, §III-A, §III-C–E, §VII-D |
| Statistical methods: tests, assumptions, CIs, effect sizes, power | Full analysis plan and per-outcome reporting (paired t, 95% CI, d_z with CI, Holm adjustment, Wilcoxon, GEE, mixed model, order effects); sensitivity analysis for power | §IV-B, §IV-E, §V, Tables III–IV |
| Numerical inconsistencies, redundant sections and tables | Text unified with the table values; sections and tables consolidated | §V, Tables III and IV |
| Qualify mechanism, calibration, automation bias, action format, generalizability | Qualified or reframed as hypotheses; limitations added | §VI, §VII, Abstract, Conclusion |
| Language, human factors linkage, separation of results and interpretation | Edited; 11 human factors references added; interpretation moved to §VI | throughout |

## Reviewer 1

**Abstract-1 (simulations and pilot not reported).** We agree. The abstract now mentions only the controlled user study, which is the only evaluation reported. The mentions of past-disaster simulations and a municipal pilot were removed from the abstract and the acknowledgment.

**Intro-1 (RQ too broad).** The RQ was narrowed to a comparison of ACHDF against a conventional dashboard in a simulated disaster-response task (§I).

**Intro-2 (roles of trust, workload, action execution).** §I now states that action execution is the primary outcome and that latency, workload, trust, and usability are secondary outcomes. Trust and workload are also design considerations, not run-time system states. See also Table I.

**Intro-3 (novelty).** Novelty is now stated as the domain-specific instantiation and empirical evaluation of JCS and adaptive-allocation principles for AI-generated recommendations. The general concept is not claimed as novel (§I, §II-A).

**Intro-4 (hypotheses missing).** Hypotheses H1 (primary, AER) and H2–H4 (secondary) are now listed in §I and referenced in §IV-E. We state them explicitly and designate the primary outcome; we do not claim that they were preregistered, and the earlier wording that they had been "defined before data collection" was removed.

**Intro-5 ("empirical link" overclaim).** Removed. The text now states that the study evaluates the integrated configuration and does not isolate components (§I, §VII-A).

**RW-1 (Section II-A weakly linked).** The former II-A (information fusion and community detection) was condensed into two sentences at the end of §II-C and linked explicitly to the input of the risk layer. The community-detection references were removed, and only two references on the information sources were kept.

**RW-2 (adaptive automation comparison).** New §II-A covers levels and types of automation, adaptive automation, and the specific ways ACHDF relates to them: no automation of action implementation, event-triggered adaptation, and adaptation of support rather than of authority.

**Sys-1 (bounded autonomy vs. escalation).** Clarified throughout. Decision authority is *not* reallocated. Only the level and form of AI support varies. §III intro, Goal 3, §III-E, and Table I were revised. Fig. 1 (the operational workflow) was redrawn so that it matches Algorithm 1 exactly: all three escalation triggers are shown, the human holds final authority in both modes, and the former "trust calibration and cognitive workload loop", which suggested run-time adaptation, was removed.

**Sys-2 (policy violation missing in Algorithm 1).** A policy-violation flag *v* from the guardrail checks was added to Algorithm 1 as a third escalation trigger, consistent with §III-E.

**Methods-1 (cues per condition; interface figure).** §IV-A and the new Table II state what each condition presents: the baseline shows hazard and risk information only; the AI-assisted condition adds an uncertainty indicator, a criticality cue, a guardrail-checked recommendation, and an escalation prompt. We added a side-by-side reconstructed illustration of the baseline, recommend-mode and escalate-mode interfaces (Fig. 2), drawn from the interface specification with the prototype's message wording, and describe the layout and the panels in §IV-A. It is a reconstruction with placeholder values, not a screenshot; no screenshots of the study interface are available (§VII-D).

**Methods-2 (task description).** §IV-C now reports the structure: 10 trials per condition (20 per participant), five response options (monitor, standby, issue alert, shelter in place, recommend evacuation), the deferral flag, and the maximum recorded latency (20.3 s). §IV-C also describes the information block of a trial, the scenario type (flood and flash flood), two example situation descriptions from the study materials (low and high risk), and the meaning of each of the five options. The per-trial uncertainty/criticality values and the per-trial time limit were not logged and are listed in §VII-D. The examples illustrate the scenario design; they cannot be matched to logged trials, because the reference actions stored for the labels S01–S10 do not follow the intended pattern (stated in §IV-C and §VII-D). The distribution of reference actions per condition is reported there as a difficulty-matching check (χ²(4) = 9.2, p = .057), together with the direction of errors (§V-A). Because difficulty matching cannot be verified, we also tested whether the result depends on it: adjusting the trial-level model for the reference action and order gives OR = 2.61 (95% CI 1.97–3.46); the AI-assisted AER is higher within every reference-action class; and re-weighting to the baseline mix leaves it at 0.81 (§V-C, Supplementary S9).

**Methods-3 (risk model).** §III-C states that the paper evaluates how the risk estimate and its uncertainty are used in the interaction, not the risk model itself. §III-C now reports the configuration of the study prototype (confirmed by the author to be that of the open reference implementation): a Bayesian linear regression on four risk factors (vulnerability entered as 1 − vulnerability; σ² = 0.10, τ² = 2.0), risk = clipped posterior mean, uncertainty = posterior variance, and recommendation bands at 0.6 and 0.8 (the 0.3 value in the configuration is not used). Calibration was not evaluated in the user study (§VII-D).

**Methods-4 (criticality and guardrails).** Criticality is defined as the severity of consequences if the recommended action is wrong or delayed (Table I). The guardrails are described as consistency, scope, and policy checks (§III-D). §III-D now reports how the guardrails are realized in the study prototype: fixed message templates selected by risk band (so the message cannot contradict the risk estimate), a case-insensitive deny-list redaction, and plain-language glossary expansion. In the prototype a deny-list hit redacts text; routing a violation to escalation is part of the framework specification and is not in the prototype configuration (stated in §III-C, §III-D and §VII-D). The criticality scale, τ_u and τ_c are not documented.

**Methods-5 (trust calibration and ergonomics: mechanism or criterion?).** Clarified. They are design considerations that shaped the interface and are measured as outcomes. They do not adapt system behavior (§III, Table I, Fig. 1 caption). The redrawn Fig. 1 (workflow) no longer shows a run-time trust/workload feedback loop, and the audit log is shown as being used only offline. The index terms now read "trust in automation" instead of "trust calibration". The conceptual layer figure of the previous version was removed to meet the page limit; §III now describes the four layers in text and names the cross-cutting element "appropriate trust" (Lee & See, 2004), consistent with Goal 2, as a design consideration that is not adapted at run time.

**Methods-6 (usability questionnaire).** Identified as the SUS (Brooke, 1996), with its scoring range (§IV-D).

**Methods-7 (AER definition).** §IV-D: in the logs, a trial is a success when the selected action equals the reference action; this reproduces the reported AER exactly. No time-out flag exists and all latencies are ≤ 20.3 s. We have not been able to document how the reference action was derived or whether it was fixed independently of the AI recommendation, so we do not claim either. AER is therefore interpreted only as agreement with the recorded scoring key, and the conclusions are limited to that definition (§IV-D, §VII-D). The time-window question is addressed by a hypothetical cutoff sensitivity analysis (§V-A); the original scoring may or may not have used a window, and the logs do not show one.

**Methods-8 (power).** No a priori analysis was conducted (stated). Sensitivity analysis: 80% power for d_z ≥ 0.40 with n = 52; observed effects on all primary and secondary outcomes exceed this (§IV-B).

**Methods-9 (statistics).** §IV-E (effect size per Lakens, 2013) gives the full analysis plan: paired t-tests on participant-level values, Holm adjustment within the secondary family, Shapiro–Wilk diagnostics with Wilcoxon confirmation, bootstrap CIs for d_z, a GEE logistic model for AER, a mixed model for log-latency, and crossover-style order/carry-over tests.

**Methods-10 (IRB).** We thank the reviewer for this point. §IV-B now contains an explicit ethics statement, and it states the situation plainly: the study was not submitted to an institutional review board (IRB), so we cannot provide an approval or exemption number. Before the study, we asked our institution's IRB about submitting it and were advised that a survey-type study with no intervention on the human body is not subject to review, and that the IRB does not accept applications for such studies. The study involved no experiment on, contact with, or intervention in the human body, and no embryos, genes, human-derived materials, drugs, or medical devices. What we can report is the following. Participation was voluntary and all participants gave informed consent and consent to the processing of their personal information before the experiment. The study consisted of a simulated decision task, post-task questionnaires, and short interviews, with no physical or medical intervention. The only personal characteristics recorded were age, gender, and technical and disaster-experience background, and the data used and shared with the paper are anonymized: identifying information was removed from the collected survey spreadsheets before analysis to protect participants' privacy, and the system logs of the task contain no identifying information. We regard the risk to participants as minimal, but we state explicitly that this is our own assessment and not a determination by an ethics body, and we list the absence of an IRB approval or exemption number as a limitation (§VII-D).

**Results-1, -2 (inconsistent numbers).** All values now come from one source, the logs (AER 0.62→0.81; latency 12.4→8.1 s; trust 3.40→4.20). The outcome-summary bar chart of the previous version was removed to meet the page limit; all values are in Table III.

**Results-3 (statistics per outcome).** Table III and §V-A/B report, for every outcome, the means and SDs, difference with 95% CI, t(51), Holm-adjusted p, and d_z with 95% CI.

**Results-4 (single Cohen's d).** Removed; effect sizes (d_z) are now given per outcome (Tables III and IV).

**Results-5 (escalated vs. non-escalated not equivalent).** §V-D is descriptive and states that the two sets are not equivalent. The previous "appropriate deferral / inappropriate reliance" rates could not be derived from the logs and were replaced by observed AER, deferral and latency (§V-D).

**Results-6 (qualitative rigor).** The interview material was not systematically coded, so it is now presented as informal observations (§IV-D, §V-E). The "mixed-method" label was removed.

**Results-7, -8 (mechanism analysis; interpretation in Results).** The former §V-F was renamed "Framework-Based Interpretation of the Results," moved to §VI-B, and explicitly described as not testing mechanisms. The Results section now contains only findings.

**Discussion-1 (action vs. risk format).** Now stated as untestable with the current design, with a factorial follow-up proposed (§VI-A).

**Discussion-2 (trust plus deferral is not calibration).** The claim was removed. §VI-C explains what calibration evidence would require.

**Discussion-3 (automation bias).** The claim was removed. The logs contain no AI recommendation or correctness field, so behavior on erroneous advice cannot be analyzed (§VI-C, §VII-D).

**Discussion-4 ("not domain-specific").** Removed. The table that mapped ACHDF principles to other domains (and its subsection) was removed; §VII-C now states that any transfer is a hypothesis, and generalization is listed as future work.

**Discussion-5 (workload→action pathway).** Reframed as a possible explanatory mechanism, noting the limitations of NASA-TLX (§VI-B).

**Limitations-1 (VII-A and VII-C overlap).** Merged into §VII-C, "Domain and Population Generalizability."

**Limitations-2 (participant population).** Added to §VII-C and §IV-B. The sample was not composed specifically of emergency-management professionals.

**Conclusion-1 (overclaims).** Rewritten. "Calibrated trust without automation bias" and "transferable design principles" were removed, and the conclusion states what was not tested.

## Reviewer 2

1. **Language.** Edited throughout. "In fact" (Introduction) and "On the other hand" (AER) were removed. The opening paragraphs of the Introduction and Sections II-B and II-C were rewritten for flow and to remove repetition with the new JCS paragraph. An incorrect running header left over from a template was replaced, and a misplaced citation (a community-detection paper cited for automation bias) was removed.
2. **Baseline description and screenshots.** See R1 Methods-1. The baseline is now described in §IV-A. No original screenshots of the study software are available; Fig. 2 and the images in Supplementary S8.4 are reconstructed illustrations and are labelled as such (§VII-D).
3. **Task detail and example.** See R1 Methods-2. Per-condition scenario counts (10 per condition) and an example logged trial record (fields, response options) are now given in §IV-C; the stimulus content of the scenarios is not stored in the records, so a full worked example is not available (§VII-D).
4. **Training.** §IV-C states that all participants were trained on the interfaces. §IV-C now describes the training content and flow (system purpose and human-in-the-loop principle, 5 min; response options and error costs, 5 min; one practice trial per interface; introduction to the questionnaires). The durations of the later steps and the total length were not recorded, and no pass criterion is documented (§VII-D).
5. **Which test, and assumptions.** §IV-E: two-sided paired t-test for every outcome; Shapiro–Wilk on the paired differences (rejected only for the trust items), with Wilcoxon signed-rank confirmation for all outcomes.
6. **Statistics next to each result.** Each outcome in §V-A/B carries its t statistic, p (Holm-adjusted for secondary outcomes), 95% CI and d_z, and Table III collects them. The collective "p < .01" paragraph was removed.
7. **Trust terminology and items.** Constructs are named consistently (perceived reliability, predictability, appropriateness; 5-point Likert; overall = mean of three items). Cronbach's α is .61 (baseline) and .46 (AI-assisted); in all AI-assisted records the logged overall score is 0.02 points above the item mean (disclosed in §IV-D; the conclusion is unchanged, +0.78 vs. +0.79); there is no published validation, and the item wording is now given in §IV-D, so the score is presented as an indicative composite (§IV-D, §VII-D).
8. **Usability questionnaire.** SUS (Brooke, 1996), ten items, 0–100 scoring; the logged overall score is a constant 2.8/4.7 points above the recomputed score in the baseline/AI-assisted condition, and both are reported (§IV-D, §V-B).
9. **Results intro paragraph and interpretive statements.** The intro was shortened to two sentences. Interpretive sentences (e.g., "helped participants transition quicker…") were removed from the Results. The former latency-distribution figure, whose caption contained an interpretive statement, was removed entirely, because it could not be verified against trial-level data.
10. **V-A/V-B redundancy.** Merged into §V-A.
11. **Table redundancy; reviewer's Table VIII not cited.** The reviewer's Tables V and VIII refer to the numbering of the previous version. In the revised manuscript, the overall outcomes are consolidated into Table III (all primary and secondary outcomes), and Table IV reports the trust items; the NASA-TLX subscale results are summarized in the text of §V-B and listed in full in the analysis output distributed with the paper. All tables are cited in the text.
12. **Ecological validity of deferral.** New §VI-D discusses forced action under uncertainty and deferral costs, and their implications for the over-reliance results.

## Reviewer 3

**Contribution 1 (action execution not novel under JCS).** We agree and thank the reviewer for pointing us to the JCS literature. Contribution 1 is now framed as *applying* the JCS principle of evaluating joint outcomes to AI disaster decision support, with action execution as the primary outcome, not as a new concept. We cite Hollnagel & Woods (2005) and Woods & Hollnagel (2006) (§I, §II-A, §III, §VI).

**Contribution 2 (ACHDF structurally similar to JCS).** We agree. ACHDF is now presented as a domain-specific instantiation of JCS and adaptive function allocation. Its novelty lies in the specific interaction design for AI-generated recommendations (uncertainty cues, guardrails, criticality- and uncertainty-triggered escalation) in disaster response.

**Contribution 3 / AER clarity.** We agree that the AER needed disentangling. §IV-D defines it from the logs (selected action = reference action) and notes that no time-out flag exists. §V-A answers the reviewer's directionality question: every unsuccessful trial was a *wrong-action* trial (198 of 520 baseline, 99 of 520 AI-assisted), and wrong and correct trials had the same latency (baseline 12.6 vs. 12.3 s; AI-assisted 8.1 vs. 8.1 s), so slowness does not explain the failures. §V-A adds a hypothetical time-cutoff sensitivity analysis (cutoffs of 10, 12, and 15 s). We also added an exploratory description of the direction of errors (§V-A): 54.5% of errors in both conditions were under-responses, errors were about two steps from the reference option on average, and both under- and over-responses were less frequent with AI support, so the improvement did not come from shifting errors to one side. How the reference action was derived is not documented (§VII-D).

**Minor 1 ("On the other hand").** Removed, and the paragraph was rewritten.

## Changes in reported values relative to the previous version
Recomputing from the logs changed some values that appeared in the previous version. The headline results (AER 0.62→0.81; latency 12.4→8.1 s; NASA-TLX 59.8→46.2; trust 3.40→4.20; SUS 68.5→81.7) are unchanged. The following differ:
- **SDs:** NASA-TLX 11.5/9.3 (previously 10.9/9.6); SUS 10.5/8.6 (previously 11.2/9.4); trust 0.57/0.45.
- **Subscales:** the previous values for four NASA-TLX subscales and three trust items do not agree with the logs and were replaced by log-based values (Table IV for the trust items; the subscale values are in the analysis output).
- **Escalation table:** the previous "appropriate deferral" and "inappropriate reliance" rates cannot be derived from the logs (no AI recommendation or correctness field) and were removed; observed deferral, AER and latency by escalation status are reported instead.
- **NASA-TLX overall:** in the logs it equals the mean of all six subscales (the earlier four-subscale inconsistency is resolved).
- **SUS:** the logged overall score is a constant 2.8 (baseline) or 4.7 (AI-assisted) points above the score recomputed from the ten items in every record; how it was obtained is not documented, so both are reported (§IV-D, §IV-F, §V-B).

## Properties of the study records
The records are the data collected in the study, as confirmed by the author, and all records and the analysis script are provided so that every reported number can be reproduced. Besides the SUS offset above, two properties of the records are reported in the manuscript (§IV-F, §VII-D) so that readers can take them into account: (i) participants' mean latencies vary little within a condition (SD about 0.8 s) and are uncorrelated across conditions, which makes the latency d_z (−3.60) extremely large, so we interpret the raw difference (about 4 s); (ii) the scenario labels S01–S10 do not map to a fixed reference action, so identical scenarios across conditions cannot be verified from the logs. We do not have contemporaneous documentation of the SUS scoring configuration or of how scenarios were assigned to labels, and we make no claim about them beyond what the records show. The abstract no longer states that failures were "wrong actions rather than slow responses" as a finding; because AER is scored as selection of the reference action, that follows from the definition, and the finding reported is that wrong and correct trials had equal latency.

## Numerical consistency
The original text and tables disagreed (AER 0.55→0.74 vs. 0.62→0.81; latency 12.3→8.0 s vs. 12.4→8.1 s; trust 3.2→4.0 vs. 3.4→4.2). The logs reproduce the **table values** (0.62/0.81; 12.4/8.1; 3.4/4.2), which are used throughout.

---

## Requests we could address only partially

For each, the manuscript states the gap explicitly and limits its conclusions accordingly.

- **Reproducibility details (R1 Methods-1–4; R2-2–R2-4).** *What we added:* a reconstructed illustration of the interfaces, the scenario information block and example situation descriptions, the training procedure, and the documented risk-model and guardrail configuration (§III-C, §III-D, §IV-A, §IV-C). After the first draft of this resubmission we also recovered materials from backup storage and re-created or re-organized them (Supplementary S8): thresholds (τ_u 0.25, τ_c 0.70), a ten-scenario design table, the training protocol with its pass criterion and completion records, and illustrative interface images. *How we use them:* because these are post hoc reconstructions that do not match the primary trial log at trial level (e.g., 208 vs. 150 escalated trials), we present them only as such, state the conflicts, and compute nothing in the manuscript from them. *What remains undocumented as contemporaneous records:* original screenshots, the per-trial values actually shown, and a design-level record of how escalation was assigned (the primary log, not the recovered table, supports the reported 150 escalated trials). We confirm that escalation in the study was pre-assigned per trial in the scenario design and not computed at run time; the paper states this and that the study therefore does not test the run-time threshold logic (§IV-C, §VII-D). Our conclusions are accordingly limited to the *presentation* of escalation, not to the threshold values. Whether the result depends on the missing materials was checked where the records allow it (Supplementary S9): the main effect holds without repeated scenarios, after adjustment for the reference action, and without the most extreme participants.
- **Reference action and time window (R3; R1 Methods-7).** We can state what the records show: AER is the share of trials whose selected action equals the recorded reference action, every unsuccessful trial was a wrong-action trial, and latency does not differ between correct and wrong trials (§IV-D, §V-A). We cannot document how the reference action was determined or whether a time window was applied in the original scoring, and the logs contain no time-out flag (§VII-D). Supplementary S8.2 gives a four-expert rating table recovered from backup (initial agreement 4/4 in five and 3/4 in five scenarios); because it is a re-organized record, the independence of the reference action from the AI recommendation rests on the author's statement and cannot be verified from the files. The manuscript therefore draws no conclusion that depends on it. What the records do allow us to test is whether the main result depends on the scoring key's composition: it does not (adjusted OR 2.61; higher AI-assisted AER within every reference-action class; first-period-only difference +0.18; 42 of 52 participants higher with AI support; Supplementary S9). These checks do not establish independence of the key from the AI recommendation, and we do not claim that.
- **Trust measure and qualitative data (R2-7; R1 Results-6).** The item wording is now reported (§IV-D); internal consistency is low (α = .46–.61). The interview data were not coded, so the mixed-method label was withdrawn.
- **Trust calibration and automation bias (R1 Discussion-2, -3).** The primary logs contain no record of the AI advice or its correctness, so neither can be assessed. A recovered, re-created log with correctness labels exists, but it does not match the primary log at trial level (same selected action in 22% of matched trials), so we do not report automation-bias rates from it (Supplementary S8.5).
- **Ethics (R1 Methods-10).** The study was not submitted for ethics review and has no approval or exemption number. Before the study, the institution's IRB advised that a survey-type study without intervention on the human body is not subject to review. The safeguards that can be reported are voluntary participation, informed consent, and anonymization (§IV-B), and the absence of a formal determination is listed as a limitation (§VII-D).

We regard these as limitations of the evidence, not as points of disagreement with the reviewers. The manuscript restricts its conclusions accordingly, and the robustness analyses in Supplementary S9 show that the primary result does not hinge on the undocumented items that the records can test: the findings concern the integrated ACHDF configuration against a dashboard, a correct-action rate as scored by the recorded key, and a short-term simulated task with a non-professional sample.

## Additional corrections from our own re-examination

Besides the reviewers' points, we re-examined the manuscript for internal consistency and over-claiming and made the following changes:

1. **Latency-distribution figure removed.** It was not reproducible from the earlier summary data and its caption contained interpretation. Trial-level latency quantiles are now reported in the text (§V-A).
2. **Deferral clarified.** The Methods state that participants could flag deferral in either condition; Algorithm 1 lists "defer" as an operator option, matching Fig. 1.
3. **Carry-over tested.** Both conditions were designed to use comparable scenarios, so carry-over cannot be ruled out, and the logs cannot verify scenario identity across conditions (§VII-D). Order and carry-over tests are in §V-C. Because those tests have limited power, we added a check that needs no assumption about carry-over: using only each participant's first period (28 AI-first vs. 24 baseline-first participants), the AER is 0.83 vs. 0.64 (difference +0.18, 95% CI 0.08–0.29, p = .001; §V-C, Supplementary S9).
4. **NASA-TLX scoring.** Resolved by the logs: the overall score is the unweighted mean of the six subscales (§IV-D).
5. **Abstract and Conclusion.** Now give the main values with effect sizes and state what the study cannot show.
6. **Over-interpretation removed.** Because the baseline had no AI support, §VI-A no longer claims that the *structure* of support, rather than its availability, explains the improvement.

## Appendix: Where each new analysis is reported
The anonymized trial-level logs (52 participants × 2 conditions × 10 trials = 1,040 trials) and questionnaire records of the study were re-analyzed with a script that produces every reported number; both are provided with the paper. Earlier drafts listed several analyses as not computable; these are now reported. Items that the records still cannot answer are listed in §VII-D.

| Item | Treatment in the manuscript |
|---|---|
| Test statistics, 95% CIs, effect sizes, assumption checks, multiplicity | Table III: for every outcome, M (SD), difference with 95% CI, paired t(51), Holm-adjusted p, d_z with bootstrap CI. Shapiro–Wilk checks, Wilcoxon confirmation, a trial-level GEE logistic model (AER) and a mixed model on log-latency (§IV-E, §V-A). |
| Power | No a priori analysis was done (stated). Sensitivity analysis: 80% power for d_z ≥ 0.40 at n = 52 (§IV-B). |
| AER definition and decomposition | In the logs, AER = share of trials with selected action = reference action; this reproduces 0.62/0.81 exactly with no time criterion. All 198 + 99 unsuccessful trials are wrong-action trials; correct and wrong trials have the same latency. A hypothetical time-cutoff sensitivity analysis is in §V-A (§IV-D). |
| Scenario count, response options, timing | 10 trials per condition, five response options, maximum recorded latency 20.3 s (§IV-C). |
| Demographics | Age, gender, technical background and disaster experience now reported (§IV-B). |
| Subscales, trust items, SUS | The three trust items with statistics (Table IV); NASA-TLX subscale ranges with effect sizes in §V-B (full table in the analysis output); Cronbach's α; SUS recomputed from items as a robustness check (§IV-D, §V-B). |
| Order effects, carry-over | Treatment × order and carry-over tests for all outcomes (§V-C). |
| Robustness to the undocumented items | First-period-only comparison, reference-action-adjusted GEE, within-stratum differences, sign and permutation tests, trimmed analysis (§V-C, Supplementary S9). |
| Escalation | 150 of 520 AI trials escalated (28.8%); descriptive comparison of AER, deferral and latency in the text of §V-D. |
| Interface comparison | Table II lists what each interface presented, and Fig. 2 is a reconstructed illustration of the interfaces. Screenshots are not available (§VII-D). |
| Risk model, guardrails, training, trust-item wording | Now documented (§III-C, §III-D, §IV-C, §IV-D). Not documented: τ_u, τ_c, criticality scale, escalation trigger in the study, total training length and pass criterion (§VII-D). |
| Qualitative coding | Still informal (§V-E). |
| Trials with erroneous AI advice | The primary logs contain no AI recommendation or correctness field, so automation bias and calibration are not assessed (§VI-C, §VII). A re-created log is not used because it does not match the primary data (Supplementary S8.5). |
| Ethics | No IRB approval or exemption number; the IRB's non-applicability advice is stated (§IV-B). |

## References added
Hollnagel & Woods (2005); Woods & Hollnagel (2006); Parasuraman, Sheridan & Wickens (2000); Kaber & Endsley (2004); Scerbo (2007); Lee & See (2004); Parasuraman & Manzey (2010); Jian, Bisantz & Drury (2000); Hart & Staveland (1988); Brooke (1996); Lakens (2013).

Note: the reviewer cited the book as "Joint Cognitive Systems: Foundations of Cognitive Systems Engineering by David Woods and Erik Hollnagel". That *Foundations* volume is by Hollnagel & Woods (2005). The companion volume *Patterns in Cognitive Systems Engineering* is by Woods & Hollnagel (2006). Both are cited.
