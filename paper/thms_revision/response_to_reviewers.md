# Response to Reviewers: THMS-26-02-0115 (Resubmission)

**Original manuscript:** "From Alerts to Actions: A Human–AI Decision System for Reliable Action Execution Under Disaster Risk," THMS-26-02-0115
**Revised title:** "From Alerts to Actions: An Action-Centered Human–AI Decision Support Framework for Disaster Response" (the word "Reliable" was removed because reliability of action execution was not measured)
**Decision letter:** 12-Nov-2026, Reject and Resubmit (Dr. L. Trajkovic, Editor-in-Chief)

## Files in this folder

| File | Content |
|---|---|
| `main.tex` | Revised manuscript |
| `main_original.tex` | Submitted version |
| `main_revised.pdf` | Compiled revised version |
| `main_diff.pdf` | latexdiff of original vs. revised (added text: blue sans-serif; deleted text: small red; tables, figures and Algorithm 1 are shown as whole old/new blocks) |
| `cover_letter_en.md` | Standalone cover letter for submission (`cover_letter_ko.md`: Korean version) |
| `cover_letter_en.pdf`, `response_to_reviewers.pdf` | Submission PDFs of the cover letter and this response, without internal repository notes (`*_ko.pdf`: Korean versions). Rebuild with `python3 make_letter_pdfs.py` |
| `reference-data.bib` | Adds 11 references (JCS, adaptive automation, trust, NASA-TLX, SUS, effect sizes) |

> **Before resubmission:** no `\TODO` items remain in `main.tex`, and the cover letter is dated. The package is ready to submit.

### How analyses requiring raw data were handled
The trial-level data and some study materials were not available for re-analysis. We did not invent any values. Every item that depends on such data is reported as far as the existing manuscript supports it, and the rest is listed explicitly in a new limitation, **§VII-D "Reporting and Analysis Limitations"**.

| Item | Treatment in the manuscript |
|---|---|
| Test statistics, 95% CIs, d_z, assumption checks, order effects, multiplicity correction | Not computable. Table V reports means, SDs where available, differences, the original significance thresholds (p < .01 / p < .05), and d_av computed from the reported means and SDs. The rest is in §VII-D. |
| SDs for AER and latency; SUS significance test | Marked "n/a" or "not reported" in Table V and listed in §VII-D. |
| Power | A post hoc sensitivity analysis was computed: with n = 52, a paired t-test at α = .05 and 80% power detects d_z ≈ 0.40. This does not need the raw data. |
| AER decomposition (correct action vs. timeliness), ground truth, time window T | The AER is now explicitly described as combining correctness and timeliness. The decomposition, ground-truth procedure and T are listed in §VII-D as unavailable. The Discussion notes that the source of the improvement (wrong vs. late actions) remains open. |
| Scenario count and composition, response options, time limit, difficulty matching, worked example, training criterion, interface screenshots | The task, procedure and both conditions are described at the level the study documentation supports. The missing details are listed in §VII-D as a reproducibility limitation. The placeholder figure was removed. |
| Risk-model estimation and calibration, criticality scale and thresholds, guardrail rules | Described conceptually (Table I, §III-C/D). Implementation details are listed in §VII-D. The evaluation is scoped to the interaction design. |
| Trust items, validation, Cronbach's α | The constructs are named consistently. The limitations (no published validation, α not estimable) are stated in §IV-E and §VII-D, and the trust score is called an "indicative composite". |
| Qualitative coding, prevalence, quotes | Reframed as informal, uncoded observations. The "mixed-method" label was dropped. |
| Number of escalated trials | Removed from Table VII and noted as unavailable. |
| Trials with erroneous AI advice | The automation-bias claim was removed. Behavior on such trials "was not analyzed" (§VI-C, §VII-B). |
| Participant demographics | Reported as in the original (age 20s–50s, mixed gender, low–high technical background, no domain expertise required). |

### Note on numerical consistency
The original text and tables disagreed (AER 0.55→0.74 vs. 0.62→0.81; latency 12.3→8.0 s vs. 12.4→8.1 s; trust 3.2→4.0 vs. 3.4→4.2). The revised manuscript uses the **table values** throughout. These could not be checked against raw data. If a check later shows the text values were correct, update Table V, §V, and Fig. 4 together.

---

## Cover letter

See `cover_letter_en.md`.

---

## Additional corrections from our own re-examination

Besides the reviewers' points, we re-examined the manuscript for internal consistency and over-claiming and made the following changes:

1. **Latency-distribution figure removed.** It could not be reproduced or verified from the available data, and showing a trial-level distribution was inconsistent with reporting that trial-level data were unavailable.
2. **Deferral clarified.** The Methods now state that participants could defer in either condition. This is consistent with Table VII, which reports deferral in non-escalated trials. Algorithm 1 now lists "defer" as an operator option, matching Fig. 2, and its unused initial assignment was removed.
3. **Carry-over acknowledged.** Both conditions used the same scenarios, so carry-over from the first condition cannot be ruled out despite counterbalancing (§IV-A, §VII-D).
4. **NASA-TLX scoring.** Only four of the six subscales are reported, and the overall score matches their mean in the baseline condition but not in the AI-assisted condition (46.2 vs. 46.0). This is now stated as a limitation (§IV-D, §VII-D).
5. **Abstract and Conclusion.** These now give the main values (AER 0.62→0.81, latency 12.4→8.1 s). They state that usability was compared only descriptively and that only significance thresholds are available.
6. **Over-interpretation removed.** Because the baseline had no AI support, §VI-A no longer claims that the *structure* of support, rather than its availability, explains the improvement.

## Associate Editor

| AE concern | Response | Location |
|---|---|---|
| Difference from JCS and adaptive function allocation | Explicit positioning as an instantiation, plus a new related-work subsection | §I (end), §II-A, §III |
| Roles and implementation of uncertainty, criticality, guardrails, escalation, trust, workload, bounded autonomy | New construct table; "bounded autonomy" defined as bounded *generation* of recommendations; trust and workload declared design considerations and outcomes, not run-time states. Implementation details that cannot be reported are stated as such. | Table I, §III-A, §III-C–E, §VII-D |
| Statistical methods: tests, assumptions, CIs, effect sizes, power | The Statistical Analysis subsection states what was done (paired tests), what is reported (means, differences, significance thresholds, d_av), and what could not be computed. A sensitivity analysis was added for power. | §IV-B, §IV-E, Table V, §VII-D |
| Numerical inconsistencies, redundant sections and tables | Text unified with the table values; sections and tables consolidated | §V, Tables V–VI |
| Qualify mechanism, calibration, automation bias, action format, generalizability | Qualified or reframed as hypotheses; limitations added | §VI, §VII, Abstract, Conclusion |
| Language, human factors linkage, separation of results and interpretation | Edited; 11 human factors references added; interpretation moved to §VI | throughout |

## Reviewer 1

**Abstract-1 (simulations and pilot not reported).** We agree. The abstract now mentions only the controlled user study, which is the only evaluation reported. The mentions of past-disaster simulations and a municipal pilot were removed from the abstract and the acknowledgment.

**Intro-1 (RQ too broad).** The RQ was narrowed to a comparison of ACHDF against a conventional dashboard in a simulated disaster-response task (§I).

**Intro-2 (roles of trust, workload, action execution).** §I now states that action execution is the primary outcome and that latency, workload, trust, and usability are secondary outcomes. Trust and workload are also design considerations, not run-time system states. See also Table I.

**Intro-3 (novelty).** Novelty is now stated as the domain-specific instantiation and empirical evaluation of JCS and adaptive-allocation principles for AI-generated recommendations. The general concept is not claimed as novel (§I, §II-A).

**Intro-4 (hypotheses missing).** Hypotheses H1 (primary, AER) and H2–H4 (secondary) are now listed in §I and referenced in §IV-E.

**Intro-5 ("empirical link" overclaim).** Removed. The text now states that the study evaluates the integrated configuration and does not isolate components (§I, §VII-A).

**RW-1 (Section II-A weakly linked).** The former II-A (information fusion and community detection) was condensed into one paragraph (§II-E) and linked explicitly to the input of the risk layer. The long list of community-detection references was reduced to two representative citations.

**RW-2 (adaptive automation comparison).** New §II-A covers levels and types of automation, adaptive automation, and the specific ways ACHDF relates to them: no automation of action implementation, event-triggered adaptation, and adaptation of support rather than of authority.

**Sys-1 (bounded autonomy vs. escalation).** Clarified throughout. Decision authority is *not* reallocated. Only the level and form of AI support varies. §III intro, Goal 3, §III-E, and Table I were revised. Fig. 2 was redrawn so that it matches Algorithm 1 exactly: all three escalation triggers are shown, the human holds final authority in both modes, and the former "trust calibration and cognitive workload loop", which suggested run-time adaptation, was removed.

**Sys-2 (policy violation missing in Algorithm 1).** A policy-violation flag *v* from the guardrail checks was added to Algorithm 1 as a third escalation trigger, consistent with §III-E.

**Methods-1 (cues per condition; interface figure).** §IV-A now states what each condition presents. The baseline shows the hazard and risk information without any AI recommendation, uncertainty indicator, criticality cue, or escalation prompt. The AI-assisted condition adds these ACHDF features, with the decision logic shown in Fig. 2 and Algorithm 1. Interface screenshots are not available and are listed as a limitation (§VII-D).

**Methods-2 (task description).** §IV-C describes the task, response types (act, choose the action, or defer when escalated) and procedure as far as documented. Scenario counts and composition, timing, and difficulty matching are not available and are listed in §VII-D as a reproducibility limitation.

**Methods-3 (risk model).** §III-C states that the paper evaluates how the risk estimate and its uncertainty are used in the interaction, not the risk model itself. Estimation and calibration details are listed in §VII-D.

**Methods-4 (criticality and guardrails).** Criticality is defined as the severity of consequences if the recommended action is wrong or delayed (Table I). The guardrails are described as consistency, scope, and policy checks (§III-D). The specific rules, scale, and thresholds are listed in §VII-D.

**Methods-5 (trust calibration and ergonomics: mechanism or criterion?).** Clarified. They are design considerations that shaped the interface and are measured as outcomes. They do not adapt system behavior (Fig. 1 caption, §III, Table I). The redrawn Fig. 2 no longer shows a run-time trust/workload feedback loop. The audit log is shown as being used only offline. The index terms now read "trust in automation" instead of "trust calibration". Fig. 1 was also redrawn: the cross-cutting element formerly labelled "Trust Calibration" is now "Appropriate Trust" (Lee & See, 2004), consistent with Goal 2, and both cross-cutting elements are marked as design considerations that are not adapted at run time.

**Methods-6 (usability questionnaire).** Identified as the SUS (Brooke, 1996), with its scoring range (§IV-D).

**Methods-7 (AER definition).** §IV-D now states explicitly that the AER combines correctness and timeliness. The ground-truth procedure, the time window, and the decomposition are not documented in enough detail and are listed in §VII-D. The Discussion notes that the source of the improvement therefore remains open.

**Methods-8 (power).** No a priori analysis was reported. We added a post hoc sensitivity analysis: 80% power for d_z ≥ 0.40 with n = 52 (§IV-B, §VII-D).

**Methods-9 (statistics).** §IV-E specifies the paired tests, the reported quantities, the d_av effect size with its formula and its limitation relative to d_z, and the analyses that could not be computed.

**Methods-10 (IRB).** §IV-B now contains an explicit ethics statement. The study was not submitted to an institutional review board or ethics committee for review. It involved only a simulated decision task and post-task questionnaires and interviews, with no physical or medical intervention. Participation was voluntary, and all participants gave informed consent.

**Results-1, -2 (inconsistent numbers).** All text values now match the tables (AER 0.62→0.81; latency 12.4→8.1 s; trust 3.4→4.2). The summary figure (Fig. 3) was regenerated from the Table V values, with one panel and scale per outcome (the former single-axis chart made the AER invisible and showed rounded differences).

**Results-3 (statistics per outcome).** Table V now reports, for every outcome, the means, SDs where available, the difference, the significance threshold of the paired test, and d_av where SDs are available. Exact test statistics and CIs could not be computed from the available data. This is stated in the table note and in §VII-D.

**Results-4 (single Cohen's d).** Removed, because it could not be attributed to a specific outcome. Effect sizes are now reported per outcome where computable (Table V).

**Results-5 (escalated vs. non-escalated not equivalent).** §V-C is now explicitly descriptive and states that the two sets of trials are not equivalent. Causal wording was removed.

**Results-6 (qualitative rigor).** The interview material was not systematically coded, so it is now presented as informal observations (§IV-D, Table VIII). The "mixed-method" label was removed.

**Results-7, -8 (mechanism analysis; interpretation in Results).** The former §V-F was renamed "Framework-Based Interpretation of the Results," moved to §VI-B, and explicitly described as not testing mechanisms. The Results section now contains only findings.

**Discussion-1 (action vs. risk format).** Now stated as untestable with the current design, with a factorial follow-up proposed (§VI-A).

**Discussion-2 (trust plus deferral is not calibration).** The claim was removed. §VI-C explains what calibration evidence would require.

**Discussion-3 (automation bias).** The claim was removed. Behavior on trials with erroneous advice was not analyzed (§VI-C, §VII-B).

**Discussion-4 ("not domain-specific").** Removed. Table II and §III-F are now labelled as hypothesized and untested, and generalization is listed as future work.

**Discussion-5 (workload→action pathway).** Reframed as a possible explanatory mechanism, noting the limitations of NASA-TLX (§VI-B).

**Limitations-1 (VII-A and VII-C overlap).** Merged into §VII-C, "Domain and Population Generalizability."

**Limitations-2 (participant population).** Added to §VII-C and §IV-B. The sample was not composed specifically of emergency-management professionals.

**Conclusion-1 (overclaims).** Rewritten. "Calibrated trust without automation bias" and "transferable design principles" were removed, and the conclusion states what was not tested.

## Reviewer 2

1. **Language.** Edited throughout. "In fact" (Introduction) and "On the other hand" (AER) were removed. The opening paragraphs of the Introduction and Sections II-B and II-D were rewritten for flow and to remove repetition with the new JCS paragraph. An incorrect running header left over from a template was replaced, and a misplaced citation (a community-detection paper cited for automation bias) was removed.
2. **Baseline description and screenshots.** See R1 Methods-1. The baseline is now described in §IV-A. Screenshots are unavailable (§VII-D).
3. **Task detail and example.** See R1 Methods-2. A worked example and per-condition scenario counts are unavailable (§VII-D).
4. **Training.** §IV-C states that all participants were trained on the interfaces. Duration, content, and any pass criterion are not documented (§VII-D).
5. **Which test, and assumptions.** §IV-E states that paired tests were used. The specific test per outcome and the assumption checks are not documented and are listed in §VII-D.
6. **Statistics next to each result.** Each outcome sentence in §V and Table V now carries its own result (significance threshold, and d_av where available). The collective "p < .01 / p < .05" paragraph at the end of the Results was removed. Exact statistics and CIs: see R1 Results-3.
7. **Trust terminology and items.** The constructs are now named consistently as perceived *reliability, predictability, appropriateness* in Table IV, §IV-D, and Table VI, and the response scale (5-point Likert) is stated. The item wording, validation, and internal consistency are not available, so the trust score is presented as an indicative composite (§IV-D, §VII-D).
8. **Usability questionnaire.** SUS, with reference and scoring range (§IV-D).
9. **Results intro paragraph and interpretive statements.** The intro was shortened to two sentences. Interpretive sentences (e.g., "helped participants transition quicker…") were removed from the Results. The former latency-distribution figure, whose caption contained an interpretive statement, was removed entirely, because it could not be verified against trial-level data.
10. **V-A/V-B redundancy.** Merged into §V-A.
11. **Tables V/VIII redundancy; Table VIII not cited.** Consolidated. Table V (outcomes) and Table VI (subscales) replace the previous Tables IV, V, VII, VIII and a duplicated table with the same label. All tables are cited in the text.
12. **Ecological validity of deferral.** New §VI-D discusses forced action under uncertainty and deferral costs, and their implications for the over-reliance results.

## Reviewer 3

**Contribution 1 (action execution not novel under JCS).** We agree and thank the reviewer for pointing us to the JCS literature. Contribution 1 is now framed as *applying* the JCS principle of evaluating joint outcomes to AI disaster decision support, with action execution as the primary outcome, not as a new concept. We cite Hollnagel & Woods (2005) and Woods & Hollnagel (2006) (§I, §II-A, §III, §VI).

**Contribution 2 (ACHDF structurally similar to JCS).** We agree. ACHDF is now presented as a domain-specific instantiation of JCS and adaptive function allocation. Its novelty lies in the specific interaction design for AI-generated recommendations (uncertainty cues, guardrails, criticality- and uncertainty-triggered escalation) in disaster response.

**Contribution 3 / AER clarity.** We agree that the AER conflates correctness and timeliness. §IV-D now says so explicitly and explains how response latency relates to it (latency describes the timing of all executed actions; the AER counts only correct actions within the time window). The trial-level data needed to separate wrong actions from late actions, and the documentation of the ground truth and the time window, were not available. We therefore report this as a limitation (§VII-D) and state in the Discussion (§VI-A) that the direction of the failures remains open.

**Minor 1 ("On the other hand").** Removed, and the paragraph was rewritten.

## References added
Hollnagel & Woods (2005); Woods & Hollnagel (2006); Parasuraman, Sheridan & Wickens (2000); Kaber & Endsley (2004); Scerbo (2007); Lee & See (2004); Parasuraman & Manzey (2010); Jian, Bisantz & Drury (2000); Hart & Staveland (1988); Brooke (1996); Lakens (2013).

Note: the reviewer cited the book as "Joint Cognitive Systems: Foundations of Cognitive Systems Engineering by David Woods and Erik Hollnagel". That *Foundations* volume is by Hollnagel & Woods (2005). The companion volume *Patterns in Cognitive Systems Engineering* is by Woods & Hollnagel (2006). Both are cited.
