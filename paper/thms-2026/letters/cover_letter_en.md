# Cover Letter (English)


---

November 19, 2026

**To:** Dr. Ljiljana Trajkovic, Editor-in-Chief
IEEE Transactions on Human-Machine Systems

**Subject:** New submission: "From Alerts to Actions: An Action-Centered Human–AI Decision Support Framework for Disaster Response"
**Previous title:** "From Alerts to Actions: A Human–AI Decision System for Reliable Action Execution Under Disaster Risk"
**Previous manuscript number:** THMS-26-02-0115 (decision of 12 November 2026: Reject and Resubmit)

---

Dear Dr. Trajkovic,

We sincerely thank you, the Associate Editor, and the three reviewers for the careful evaluation of manuscript THMS-26-02-0115. As invited in your decision letter of 12 November 2026, we have considered every comment and now submit a substantially revised manuscript as a new submission.

The Associate Editor identified three main concerns: the novelty of the contribution, methodological transparency, and the alignment of the claims with the evidence. We agree with these concerns. In particular, we accepted Reviewer 3's observation about the Joint Cognitive Systems (JCS) literature and have fundamentally repositioned the paper. The revised manuscript no longer presents action-centered evaluation as a new concept. Instead, it presents a concrete application of established human factors principles to AI-based disaster decision support, together with an empirical evaluation.

The main changes are as follows.

1. **Positioning and contributions.** ACHDF is now explicitly framed as an instantiation, for disaster response, of the JCS perspective (Hollnagel & Woods, 2005; Woods & Hollnagel, 2006) and of adaptive function allocation (Parasuraman et al., 2000; Kaber & Endsley, 2004; Scerbo, 2007). A new Related Work subsection (II-A) explains how ACHDF relates to this body of work, and all three contributions have been rewritten.

2. **Definition of constructs.** A new Table I gives the role and operational definition of uncertainty, criticality, guardrails, bounded autonomy, escalation, trust, workload, and action execution, distinguishing design inputs, system modes, design considerations, and outcomes. Throughout the manuscript, we now state consistently that ACHDF adapts only the *level and form of AI support*, and that decision authority always remains with the human operator.

3. **Methodological transparency.** We now describe what each condition presented (Table II and a reconstructed illustration of both interfaces), the decision task (10 trials per condition, five response options with their explained meaning), the training procedure, the risk-model and guardrail configuration, the participants (full demographics), and all instruments (NASA-TLX with six subscales, a three-item trust measure with consistent terminology, and the SUS). We define the Action Execution Rate (AER) from the trial logs and separate correctness from timeliness: all unsuccessful trials were wrong actions rather than late ones. Details that the study records still do not document (interface screenshots, per-trial scenario values, how the reference action was derived, total training length and pass criterion, the escalation thresholds and criticality scale) are listed explicitly in Section VII-D rather than omitted.

4. **Statistics.** The anonymized trial-level logs and questionnaire records have been re-analyzed and are provided with the paper together with the analysis scripts. For every outcome, Table III now reports means and SDs, the paired difference with its 95% CI, the paired t statistic, the Holm-adjusted p value, and the effect size d_z with its CI. The Methods specify the tests, assumption checks (Shapiro–Wilk, with Wilcoxon confirmation), a trial-level logistic and a mixed model as sensitivity analyses, order and carry-over tests, and a power sensitivity analysis. Recomputation changed some secondary values; these changes are listed in the response letter.

5. **Consistency and redundancy.** Numerical inconsistencies between the text and the tables have been corrected, and all values now come from a single analysis of the logs. Overlapping Results subsections (former V-A/V-B) were merged, redundant tables were consolidated, and the single Cohen's d whose comparison was unclear was removed. The "appropriate deferral" and "inappropriate reliance" rates of the previous version could not be derived from the logs and were replaced by observed deferral, AER and latency.

6. **Qualified claims.** Claims regarding mechanism, trust calibration, automation bias, the benefit of the action format, and cross-domain generalizability have been removed or reframed as hypotheses. Correspondingly, the Limitations section is reorganized around four points: the bundled intervention, the absence of a direct test of calibration and automation bias, domain and population generalizability, and reporting limitations (including missing study materials, the absence of an IRB approval or exemption number, and the short-term design); the ecological validity of deferral is in Section VI-D. The title no longer contains "Reliable", because reliability of action execution was not measured.

7. **Structure and language.** The Results section now reports only descriptive and inferential findings. The former "mechanism analysis" has been moved to the Discussion and recast as a framework-based interpretation (Section VI-B). The manuscript has been edited for clarity and flow, inappropriate transitions ("in fact", "on the other hand") have been removed, and eleven references from the human factors literature have been added. The manuscript was shortened to the 10-page limit for regular papers; no reviewer point was dropped.

**Ethics.** The study was not submitted to an IRB because our institution's IRB advised that survey-type studies without intervention on the human body are not subject to review; consent and anonymization are described in Section IV-B.

A detailed point-by-point response to the reviewers and a marked-up comparison of the original and revised manuscripts (latexdiff) are enclosed. We believe the revision has made the contribution and its evidential basis considerably clearer, and we would be grateful for your further consideration.

Sincerely,

Geunsik Lim

---

Geunsik Lim
Department of Electrical and Computer Engineering, Sungkyunkwan University
2066, Seobu-ro, Jangan-gu, Suwon 16419, Republic of Korea

**Enclosures:** (1) Revised manuscript; (2) Point-by-point response to reviewers; (3) Marked-up comparison of original and revised manuscripts (latexdiff)
