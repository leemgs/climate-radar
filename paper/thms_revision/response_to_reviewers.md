# Response to Reviewers: THMS-26-02-0115 (Resubmission)

**Original manuscript:** "From Alerts to Actions: A Human–AI Decision System for Reliable Action Execution Under Disaster Risk," THMS-26-02-0115
**Decision letter:** 12-Nov-2026, Reject and Resubmit (Dr. L. Trajkovic, Editor-in-Chief)

## Files in this folder

| File | Content |
|---|---|
| `main.tex` | Revised manuscript |
| `main_original.tex` | Submitted version (for diffing: `latexdiff main_original.tex main.tex > diff.tex`) |
| `main_revised.pdf` | Compiled revised version. TODO items appear in **red** |
| `reference-data.bib` | Adds 11 references (JCS, adaptive automation, trust, NASA-TLX, SUS, effect sizes) |

> **Before resubmission:** the revised manuscript contains 51 `\TODO{...}` markers (shown in red). Each one needs data or facts that only the author has: tests, CIs, scenario details, IRB, screenshots, and so on. No numbers were invented. Search for `\TODO` in `main.tex` and remove the `\newcommand{\TODO}` line from the preamble once all are resolved.

### Author checklist (items that need data)
1. **Statistics:** for each outcome, the test, statistic, exact p, 95% CI, and d_z (Table V). Also order effects and Holm correction.
2. **AER decomposition:** correct-action rate, on-time rate, and the distribution of the three failure types (Reviewer 3).
3. **Ground truth and time window T** for "appropriate action". Confirm it is independent of the AI recommendation.
4. **Scenarios:** number per condition, response options, time limit, uncertainty/criticality composition, difficulty matching, and one worked example.
5. **Erroneous AI recommendations:** did any trials include them? (Decides whether the automation-bias sentence stays.)
6. **Interface screenshots** for Fig. 3 (baseline / recommend / escalate).
7. **Risk model** (estimator, calibration), **criticality** scale and thresholds, and **guardrail** implementation details.
8. **Participants:** demographics, expertise, recruitment source, **IRB number**, compensation, power or sensitivity analysis.
9. **Training:** duration, content, pass criterion.
10. **Trust questionnaire:** item wording, source, and Cronbach's α. Confirm the standard **SUS** was used. Raw vs. weighted TLX.
11. **Qualitative coding:** procedure, κ, theme prevalence, quotes.
12. **Figures:** check that `fig_workload_trust_summary.png` (Fig. 5) shows the reconciled values (AER 0.62→0.81, latency 12.4→8.1 s, trust 3.4→4.2). Also check whether `fig_system_overview.png` contains wording like "shifts decision authority". If so, change it to "level of AI support".
13. **Number reconciliation:** the revised text uses the **table values** (AER 0.62/0.81, latency 12.4/8.1 s, trust 3.4/4.2). The old text values (0.55/0.74, 12.3/8.0 s, 3.2/4.0) were removed. **Verify both against the raw data.**

---

## Cover letter (draft)

Dear Dr. Trajkovic,

We thank you, the Associate Editor, and the three reviewers for the thorough evaluation of manuscript THMS-26-02-0115. As invited in the decision letter of 12 November 2026, we submit a substantially revised manuscript as a new submission. The main changes are:

1. **Positioning and contribution.** ACHDF is now explicitly framed as an instantiation of the Joint Cognitive Systems perspective (Hollnagel & Woods, 2005; Woods & Hollnagel, 2006) and of adaptive function allocation (Parasuraman et al., 2000; Kaber & Endsley, 2004; Scerbo, 2007). A new Related Work subsection (II-A) states how ACHDF relates to this work. All three contributions were reworded so that we no longer claim action-oriented evaluation as a new concept.
2. **Construct definitions.** A new Table I defines the role (design input, system mode, design consideration, outcome) and operationalization of uncertainty, criticality, guardrails, bounded autonomy, escalation, trust, workload, and action execution. The manuscript now states consistently that ACHDF adapts the *level and form of AI support* and that decision authority always remains with the human.
3. **Methods transparency.** New subsections and figures describe both interfaces, the task and scenarios (with a worked example), training, participants and ethics approval, power, and all instruments (NASA-TLX, a three-item trust measure with consistent terminology, SUS).
4. **Statistics.** A new Statistical Analysis subsection specifies tests, assumption checks, 95% CIs, named effect sizes (d_z / rank-biserial), multiplicity correction, and order-effect analysis. Each outcome is now reported with its statistics in one table (Table V).
5. **Consistency and redundancy.** Numerical inconsistencies between text and tables were corrected. Former Sections V-A/V-B were merged. Former Tables V/VII/VIII and the duplicate workload/trust table were consolidated into Tables V and VI. The ambiguous single Cohen's d was removed.
6. **Qualified claims.** Claims about mechanism, trust calibration, automation bias, the benefit of the action format, and cross-domain generalizability were removed or explicitly reframed as hypotheses. Corresponding limitations were added (bundled intervention, no direct calibration or automation-bias test, domain and population generalizability, ecological validity of deferral).
7. **Structure and language.** Results now contain only descriptive and inferential findings. The former "mechanism analysis" moved to the Discussion as a framework-based interpretation (VI-B). The manuscript was edited for language, including removing "in fact" and "on the other hand".

Sincerely,
Geunsik Lim

---

## Associate Editor

| AE concern | Response | Location |
|---|---|---|
| Difference from JCS and adaptive function allocation | Explicit positioning as an instantiation, plus a new related-work subsection | §I (end), §II-A, §III |
| Roles and implementation of uncertainty, criticality, guardrails, escalation, trust, workload, bounded autonomy | New construct table; "bounded autonomy" defined as bounded *generation* of recommendations; trust and workload declared design considerations and outcomes, not run-time states | Table I, §III-A, §III-D–F |
| Statistical methods: tests, assumptions, CIs, effect sizes, power | New subsection plus per-outcome table | §IV-F, §IV-B, Table V |
| Numerical inconsistencies, redundant sections and tables | Fixed and consolidated | §V, Tables V–VI |
| Qualify mechanism, calibration, automation bias, action format, generalizability | Qualified or reframed as hypotheses; limitations added | §VI, §VII, Abstract, Conclusion |
| Language, human factors linkage, separation of results and interpretation | Edited; 11 human factors references added; interpretation moved to §VI | throughout |

## Reviewer 1

**Abstract-1 (simulations and pilot not reported).** We agree. The abstract now mentions only the controlled user study, which is the only evaluation reported. The mentions of past-disaster simulations and a municipal pilot were removed from the abstract and the acknowledgment.

**Intro-1 (RQ too broad).** The RQ was narrowed to a comparison of ACHDF against a conventional dashboard in a simulated disaster-response task (§I).

**Intro-2 (roles of trust, workload, action execution).** §I now states that action execution is the primary outcome and that latency, workload, trust, and usability are secondary outcomes. Trust and workload are also design considerations, not run-time system states. See also Table I.

**Intro-3 (novelty).** Novelty is now stated as the domain-specific instantiation and empirical evaluation of JCS and adaptive-allocation principles for AI-generated recommendations. The general concept is not claimed as novel (§I, §II-A).

**Intro-4 (hypotheses missing).** Hypotheses H1 (primary, AER) and H2–H4 (secondary) are now listed in §I and referenced in §IV-F.

**Intro-5 ("empirical link" overclaim).** Removed. The text now states that the study evaluates the integrated configuration and does not isolate components (§I, §VII-A).

**RW-1 (Section II-A weakly linked).** The former II-A (information fusion and community detection) was condensed into one paragraph (§II-E) and linked explicitly to the input of the risk layer.

**RW-2 (adaptive automation comparison).** New §II-A covers levels and types of automation, adaptive automation, and the specific ways ACHDF relates to them: no automation of action implementation, event-triggered adaptation, and adaptation of support rather than of authority.

**Sys-1 (bounded autonomy vs. escalation).** Clarified throughout. Decision authority is *not* reallocated. Only the level and form of AI support varies. The Fig. 2 caption, §III intro, Goal 3, §III-F, and Table I were revised.

**Sys-2 (policy violation missing in Algorithm 1).** A policy-violation flag *v* from the guardrail checks was added to Algorithm 1 as a third escalation trigger, consistent with §III-F.

**Methods-1 (cues per condition; interface figure).** §IV-A describes the information and cues in each condition, and new Fig. 3 shows both interfaces. *[Author: insert screenshots and complete the dashboard description.]*

**Methods-2 (task description).** New §IV-C covers number and structure of scenarios, response options, timing, uncertainty/criticality composition, difficulty matching, and a worked example. *[Author data.]*

**Methods-3 (risk model).** §III-C now specifies the requirements. *[Author: model class, uncertainty estimator, calibration. State whether the risk values were scripted in the experiment.]*

**Methods-4 (criticality and guardrails).** Criticality is defined as the severity of consequences if the recommended action is wrong or delayed (Table I). The guardrails are specified as consistency, scope, and policy checks (§III-D). *[Author: confirm details, scale, thresholds.]*

**Methods-5 (trust calibration and ergonomics: mechanism or criterion?).** Clarified. They are design considerations that shaped the interface and are measured as outcomes. They do not adapt system behavior (Fig. 1 caption, §III, Table I).

**Methods-6 (usability questionnaire).** Identified as the SUS (Brooke, 1996), with scoring (§IV-E).

**Methods-7 (AER definition).** §IV-E defines the ground truth (independent reference protocol), the time window *T*, and a decomposition into correct-action rate and on-time rate with three failure categories. *[Author data.]*

**Methods-8 (power).** Added to §IV-B. *[Author: a priori power analysis or sensitivity analysis.]*

**Methods-9 (statistics).** New §IV-F.

**Methods-10 (IRB).** Added to §IV-B. *[Author: committee and approval number.]*

**Results-1, -2 (inconsistent numbers).** All text values now match the tables (AER 0.62→0.81; latency 12.4→8.1 s; trust 3.4→4.2). The table values were verified against the raw data. *[Author: verify before submission.]*

**Results-3 (statistics per outcome).** Table V reports the test, statistic, p, 95% CI, and effect size for each outcome.

**Results-4 (single Cohen's d).** Removed. Each outcome now has its own effect size (Table V).

**Results-5 (escalated vs. non-escalated not equivalent).** §V-C is now explicitly descriptive and states that the two sets of trials are not equivalent. Causal wording was removed.

**Results-6 (qualitative rigor).** §IV-E describes the coding procedure. Table VIII adds prevalence and representative quotations. *[Author data. If coding evidence is unavailable, we will remove the "mixed-method" label. That label has already been removed from the abstract.]*

**Results-7, -8 (mechanism analysis; interpretation in Results).** The former §V-F was renamed "Framework-Based Interpretation of the Results," moved to §VI-B, and explicitly described as not testing mechanisms. The Results section now contains only findings.

**Discussion-1 (action vs. risk format).** Now stated as untestable with the current design, with a factorial follow-up proposed (§VI-A).

**Discussion-2 (trust plus deferral is not calibration).** The claim was removed. §VI-C explains what calibration evidence would require.

**Discussion-3 (automation bias).** The claim was removed. Automation bias requires trials with erroneous advice (§VI-C, §VII-B).

**Discussion-4 ("not domain-specific").** Removed. Table II and §III-G are now labelled as hypothesized and untested, and generalization is listed as future work.

**Discussion-5 (workload→action pathway).** Reframed as a possible explanatory mechanism, noting the limitations of NASA-TLX (§VI-B).

**Limitations-1 (VII-A and VII-C overlap).** Merged into §VII-C, "Domain and Population Generalizability."

**Limitations-2 (participant population).** Added to §VII-C and §IV-B.

**Conclusion-1 (overclaims).** Rewritten. "Calibrated trust without automation bias" and "transferable design principles" were removed, and the conclusion states what was not tested.

## Reviewer 2

1. **Language.** Edited throughout. "In fact" (Introduction) and "On the other hand" (AER) were removed. The opening paragraphs of the Introduction and Sections II-B and II-D were rewritten for flow and to remove repetition with the new JCS paragraph. An incorrect running header left over from a template was replaced, and a misplaced citation (a community-detection paper cited for automation bias) was removed.
2. **Baseline description and screenshots.** See R1 Methods-1: §IV-A and Fig. 3.
3. **Task detail and example.** See R1 Methods-2: §IV-C, with a worked example and the number of scenarios per condition.
4. **Training.** New §IV-D covers duration, content, and the comprehension criterion. *[Author data.]*
5. **Which test, and assumptions.** §IV-F covers Shapiro–Wilk and Q–Q checks, paired t vs. Wilcoxon, and the test per outcome in Table V.
6. **Statistics next to each result.** Each outcome sentence in §V and Table V now carries its statistic, p, and CI. The collective "p < .01" paragraph was removed.
7. **Trust terminology and items.** The constructs are now named consistently as perceived *reliability, predictability, appropriateness* in Table IV, §IV-E, and Table VI. Item wording, scale, scoring, source (e.g., Jian et al., 2000), and Cronbach's α were added. *[Author data.]*
8. **Usability questionnaire.** SUS, with reference and scoring (§IV-E).
9. **Results intro paragraph and interpretive statements.** The intro was shortened to two sentences. Interpretive sentences (e.g., "helped participants transition quicker…") were removed from the Results, and so was the interpretive part of the Fig. 4 caption.
10. **V-A/V-B redundancy.** Merged into §V-A.
11. **Tables V/VIII redundancy; Table VIII not cited.** Consolidated. Table V (outcomes plus statistics) and Table VI (subscales) replace the previous Tables IV, V, VII, VIII and a duplicated table with the same label. All tables are cited in the text.
12. **Ecological validity of deferral.** New §VI-D discusses forced action under uncertainty and deferral costs, and their implications for the over-reliance results.

## Reviewer 3

**Contribution 1 (action execution not novel under JCS).** We agree and thank the reviewer for pointing us to the JCS literature. Contribution 1 is now framed as *applying* the JCS principle of evaluating joint outcomes to AI disaster decision support and operationalizing it (with the AER decomposed), not as a new concept. We cite Hollnagel & Woods (2005) and Woods & Hollnagel (2006) (§I, §II-A, §III, §VI).

**Contribution 2 (ACHDF structurally similar to JCS).** We agree. ACHDF is now presented as a domain-specific instantiation of JCS and adaptive function allocation. Its novelty lies in the specific interaction design for AI-generated recommendations (uncertainty cues, guardrails, criticality- and uncertainty-triggered escalation) in disaster response.

**Contribution 3 / AER clarity.** AER is now fully specified: (a) "appropriate" means a reference action defined in advance and independently of the AI; (b) the time window is a fixed *T*; (c) AER is decomposed into the correct-action rate and the on-time rate; and (d) failures are classified as wrong action, late correct action, or no action. This shows whether failures stem from taking too long or from taking the wrong action (§IV-E, Table IV, Table V, §V-A).

**Minor 1 ("On the other hand").** Removed, and the paragraph was rewritten.

## References added
Hollnagel & Woods (2005); Woods & Hollnagel (2006); Parasuraman, Sheridan & Wickens (2000); Kaber & Endsley (2004); Scerbo (2007); Lee & See (2004); Parasuraman & Manzey (2010); Jian, Bisantz & Drury (2000); Hart & Staveland (1988); Brooke (1996); Lakens (2013).

Note: the reviewer cited the book as "Joint Cognitive Systems: Foundations of Cognitive Systems Engineering by David Woods and Erik Hollnagel". That *Foundations* volume is by Hollnagel & Woods (2005). The companion volume *Patterns in Cognitive Systems Engineering* is by Woods & Hollnagel (2006). Both are cited.
