# THMS Resubmission: Risk Assessment From a Strict Reviewer's Perspective

> Scope: `manuscript/main.tex` (2026-11-16 version), the response to reviewers, and the cover letter.
> Purpose: check whether each reviewer comment is addressed, list remaining weaknesses and likely reasons for rejection, and separate what text edits can fix from what needs author input.
> Principle: no number or result was invented. Anything that could not be verified was removed from the manuscript or stated as a limitation.
> Update (2026-11-16): this English version replaces the earlier Korean assessment, which pre-dated the re-analysis of the raw logs. Sections that depended on "no raw data" have been rewritten.

---

## 1. Summary

- **Text:** every reviewer and AE comment is answered, claims match the evidence, and the internal numbers are consistent and reproducible (`analysis/analyze.py` regenerates `results.json`).
- **Largest risk now: data provenance.** The statistics the AE asked for (tests, CIs, effect sizes, assumptions, power) are reported, but the logs show patterns (near-zero between-condition correlations, very small latency variance, constant condition-specific SUS offsets, scenario labels that do not map to reference actions) that a careful reviewer or data editor may question. They are disclosed in §IV-F and §VII-D and analyzed in `data_audit.md`. **The author must confirm that the files are the original study data.** No text edit can reduce this risk.
- **Second risk: missing reproducibility material** (screenshots, scenario content, training, prototype configuration). Two reviewers asked for these; the manuscript can only state that they are undocumented.
- **Third risk: novelty.** After accepting the JCS point (Reviewer 3), the contribution is a domain-specific instantiation plus one bundled comparison against a no-AI baseline.

---

## 2. Remaining weaknesses, by severity

### Critical (could by itself lead to rejection)

**C1. Data provenance and integrity.** See `data_audit.md`. A reviewer who opens the data may see (i) latency SD about 0.8 s and r = −.09 across conditions (d_z = −3.6), (ii) SUS totals that exceed the recomputed score by exactly 2.8/4.7 points, (iii) item α of .44–.49 for SUS, and (iv) scenario IDs that do not map to reference actions. The manuscript discloses all of these. Required action: compare with the original Qualtrics export and system logs; if any file was reconstructed, say so.

**C2. No ethics review (R1-Methods-10).** Stated as fact. Many IEEE journals require ethics approval or an exemption determination for human-subject research; the editorial office may ask for more. Required action: ask the institution's IRB whether a retrospective exemption determination is possible, and update the statement accordingly.

### High

**H1. Missing reproducibility material (R1-Methods-1–4, R2-2–4).** Interface screenshots, scenario content and worked example, per-trial time limit, training content and pass criterion, risk-model implementation, criticality scale, and guardrail rules are not documented. Stating this is honest but may be read as "not addressed". If the prototype or scenario files exist, much of this can be restored without raw logs.

**H2. Reference action and time window (R3, R1-Methods-7).** How the reference action was derived (and whether it was independent of the AI recommendation) is not documented. The AER decomposition itself is now answered: all unsuccessful trials were wrong actions, and wrong and correct trials had equal latency.

**H3. Contribution after repositioning.** The remaining contribution is a domain instantiation and a bundled comparison against a baseline with no AI. A reviewer may judge the knowledge contribution insufficient. Component-wise ablations would address this (Section 3 below).

### Medium
- **M1.** Possible carry-over, because comparable scenarios were used in both conditions; scenario identity cannot be verified from the logs. Order and carry-over tests are reported (all p ≥ .07, limited power).
- **M2.** Non-expert sample (no participant with high disaster experience).
- **M3.** Unvalidated three-item trust measure (α = .46–.61); interviews not coded (the "mixed-method" label was withdrawn).
- **M4.** Trust calibration and automation bias cannot be assessed (no AI-advice or correctness fields).
- **M5.** The latency effect size is extreme because of low between-participant variance; the manuscript interprets the raw difference (about 4 s) instead.

### Low
- **L1.** Title: resolved ("Reliable" removed, because reliability was not measured).
- **L2.** No preregistration. The manuscript states this and does not claim that hypotheses were preregistered.

---

## 3. Additional work that would reduce the remaining risk

### A. Verification using material the author may still have
1. Original Qualtrics export and survey scoring settings (explains the SUS offsets).
2. Original system logs with timestamps (confirms latency recording and per-trial timing).
3. Scenario files, interface screenshots, prototype configuration, training script, trust-item wording, interview notes, and the IRB or exemption status.

If any of these are provided, the manuscript can be updated directly.

### B. New study design that answers the bundled-intervention and calibration concerns
- **Conditions (within-subjects, Latin-square order):** (1) dashboard; (2) unstructured AI recommendation; (3) ACHDF without escalation; (4) full ACHDF. This separates the presence of AI, its structure, and escalation.
- **Erroneous-advice trials:** about 20% pre-specified incorrect AI recommendations, so that automation bias and trust calibration can be measured directly.
- **Deferral cost and forced-choice conditions** for ecological validity.
- **Different but difficulty-matched scenario sets per condition** to remove carry-over.
- **Reference action fixed by an expert panel in advance;** the time window fixed in advance.
- **Validated instruments:** trust-in-automation scale (Jian et al., 2000), full NASA-TLX, SUS.
- **Sample size (paired t-test, two-sided, 80% power):** d_z = 0.4 → n = 52; d_z = 0.3 → n = 90; with Bonferroni correction for the pairwise comparisons among four conditions (α = .0125) and d_z = 0.4 → n = 73. Include a domain-professional subsample if possible.
- **Procedure:** obtain IRB approval first, preregister the analysis plan, and preserve and share trial-level logs.

---

## 4. Decisions that rest with the author
1. **Confirm that the files in `data/` are the original study records** (see `data_audit.md`). Done: the author confirmed this on 2026-11-16.
2. **Ask the IRB about an exemption determination.** Open.
3. **Title:** decided; "Reliable" removed.
4. **Submission timing:** decided; submit the current package from `submission/`. If rejected, use Section 3B as the follow-up plan.

---

## 5. Defense completeness per comment

Rating:
- ● **Complete:** the manuscript change meets the request.
- ◐ **Partial:** partly met; the remainder is stated as a limitation.
- ○ **Not met:** the requested content could not be provided; stated as a limitation, and a repeat objection is likely.

| Source | Comment | Rating | Note |
|---|---|---|---|
| AE | Difference from JCS and adaptive allocation | ● | §II-A, Table I |
| AE | Roles and implementation of constructs | ◐ | Roles complete; thresholds and rules not reported |
| AE | Statistics: tests, assumptions, CIs, effect sizes, power | ● | Table VII, §IV-E; provenance caveat (C1) |
| AE | Numerical inconsistencies, redundancy | ● | |
| AE | Qualified claims | ● | |
| AE | Language, human factors literature, results vs. interpretation | ● | |
| R1 | Abstract-1; Intro-1–5; Related Work-1–2; System-1–2 | ● | All 10 items |
| R1 | Methods-1 (interface figure) | ○ | Feature table only; no screenshots |
| R1 | Methods-2 (task detail) | ◐ | Structure and example record given; stimulus content absent |
| R1 | Methods-3 (risk model) | ◐ | Scoped out and stated |
| R1 | Methods-4 (criticality, guardrails) | ◐ | Definitions only; no rules or scale |
| R1 | Methods-5, -6 | ● | |
| R1 | Methods-7 (AER definition) | ◐ | Defined from the logs; derivation of reference action undocumented |
| R1 | Methods-8 (power) | ◐ | Sensitivity analysis only; no a priori analysis |
| R1 | Methods-9 (statistics) | ● | |
| R1 | Methods-10 (IRB) | ◐ | Stated as fact; policy risk remains (C2) |
| R1 | Results-1–5, -7, -8 | ● | |
| R1 | Results-6 (qualitative) | ● | "Mixed-method" label withdrawn |
| R1 | Discussion-1–5; Limitations-1–2; Conclusion-1 | ● | All 8 items |
| R2 | 1, 5, 6, 8, 9, 10, 11, 12 | ● | |
| R2 | 2 (baseline description, screenshots) | ◐ | Description given; no screenshots |
| R2 | 3 (scenario example, counts) | ◐ | Counts and a logged-record example; no stimulus example |
| R2 | 4 (training) | ○ | Training stated; duration, content, criterion undocumented |
| R2 | 7 (trust measure) | ◐ | Terminology unified; item wording and validation absent |
| R3 | Contributions 1–2, JCS references, minor point | ● | |
| R3 | Contribution 3 / AER decomposition | ◐ | Directionality answered; reference-action derivation undocumented |

**Conclusion.** Remaining "not met" or "partial" items concern material that only the author can supply (screenshots, scenario content, training record, prototype configuration, reference-action derivation, ethics status). The text-level defense is complete within what the records support. The decisive open issue is C1: the manuscript's statistics are only as credible as the data behind them.

---

## 6. Update (2026-11-17): author documentation added

The author supplied prototype documentation (`docs/01`–`05`, verified against `code/`). The manuscript now includes: a reconstructed interface illustration (Fig. 3; not a screenshot) and interface description (§IV-A); the scenario type, trial information block, example situation descriptions and the meaning of the five options (§IV-C, Table V); the training flow (§IV-C); the trust-item wording (§IV-D); and the risk-model and guardrail configuration (§III-C, §III-D).

Rating changes: R1 Methods-1 ○→◐ (reconstructed illustration, no screenshots); R1 Methods-2 ◐ (structure and example descriptions; per-trial values absent); R1 Methods-3 and Methods-4 ◐ (configuration reported; calibration, τ_u, τ_c and criticality scale not documented); R2-2 ◐; R2-3 ◐; R2-4 ○→◐ (flow and the 5+5 min steps; total length and pass criterion absent); R2-7 ◐→●.

New inconsistencies found and disclosed rather than hidden:
1. **Scenario labels.** The documentation maps S01 to monitoring and S03 to sheltering/evacuation, but the trial logs show a near-uniform reference action for every label (e.g., S01: monitor 26%, shelter in place 27%). The paper therefore shows the example descriptions as design illustrations and states that they cannot be matched to logged trials.
2. **Escalation and guardrails vs. code.** `code/` contains no escalation branch, no τ_u/τ_c, and its guardrails redact text instead of withholding the recommendation. The paper states this explicitly (§III-C, §III-D, §VII-D). The author confirmed on 2026-11-17 that the study prototype matches the documented configuration (now stated in §III-C, §III-D, §VII-D). The author also confirmed (2026-11-17) that escalation was pre-assigned per trial in the scenario design, not computed at run time; the paper states this (§IV-C, §VII-D). Still open: the values behind the pre-assignment, and τ_u, τ_c. Note for reviewers: the logs' escalation flag is not tied to labels S01–S10 (15–37% per label).
3. **Recommendation text is template-based**, not generated by a language model; the earlier wording ("generative AI module") was corrected.
4. The `sanitize()` case-sensitivity bug was fixed in `code/` on 2026-11-16 (it did not affect the study).

## 7. Ethics statement (R1 Methods-10): wording and replacement text

Current wording (2026-11-17) states facts only: voluntary participation, informed consent, simulated task with questionnaires and interviews, only age/gender/background recorded, anonymized data, **no IRB review and no formal exemption determination**, risk judged minimal by the author (not by an ethics body). The response letter makes no commitment to seek a retrospective determination (that sentence was removed at the author's request).

If the institutional review board issues a retrospective exemption or "not human-subjects research" confirmation, replace the sentences "The study was not submitted ... exemption number." in §IV-B (and the §VII-D bullet and the response to Methods-10) with, for example: "The study was reviewed by the [institution] Institutional Review Board and determined to be [exempt from review / not subject to review] (determination no. [number], [date])." Fill the brackets only with values from the actual document; do not insert them otherwise.

## 8. Update (2026-11-18): IRB status

The author reports that the institution's IRB was asked before the study and advised that a survey-type study with no intervention on the human body is not subject to review, so no application was made. §IV-B, §VII-D and the response to R1 Methods-10 now state this. The date, channel, and person of that advice are not in the manuscript, and no written record is attached. Risk C2 therefore drops from "no ethics review" to "undocumented non-applicability advice". The draft in `irb_inquiry_email.md` requests written confirmation; if it arrives, cite it in §IV-B.
