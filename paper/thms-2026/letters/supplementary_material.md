# Supplementary Material

**Manuscript:** "From Alerts to Actions: An Action-Centered Human–AI Decision Support Framework for Disaster Response"

This document collects the study materials that the author's prototype documentation provides, in more detail than the page limit of the manuscript allows. It contains no new results. Everything not documented is listed explicitly in Section S7.

## S1. Interface specification

| Element | Baseline (dashboard) | AI-assisted (ACHDF) |
|---|---|---|
| Hazard and risk information | yes | yes |
| Explicit uncertainty indicator | no | yes |
| Criticality cue | no | yes |
| Guardrail-checked action recommendation | no | yes ("recommend" mode) |
| Escalation prompt with evidence and options | no | yes ("escalate" mode; 150 of 520 trials, 28.8%) |
| Human decides and executes | yes | yes |

**Baseline layout.** Risk-level summary (value and color coding) at the top, a map or time series of risk indicators in the center, and the five response buttons (monitor, standby, issue alert, shelter in place, recommend evacuation) below. No uncertainty, criticality, or recommendation text.

**Recommend mode.** Risk score and uncertainty indicator (confidence interval or variance proxy), a criticality badge, and one guardrail-checked recommendation with a short rationale. The five options remain selectable, so the recommendation can be ignored. The prototype's message templates are:

- High risk: "IMMEDIATE: Move to nearest shelter; bring ID, water, and phone."
- Medium risk: "PREPARE: Pack essentials, confirm route to shelter, check on neighbors."
- Low risk: "STAY ALERT: Monitor updates; avoid low-lying areas."
- Subgroup sentences: elderly, "If mobility is limited, call local support or ask a neighbor for assistance."; migrant, "Multilingual help is available at the community center."

**Escalate mode.** Instead of a single recommendation, the interface shows the evidence and options together with a prompt that human review is required because of uncertainty, criticality, or a policy issue. The participant chooses an action or sets the deferral flag.

**Common elements.** Risk score and variance, a deferral flag ("flag for further confirmation"), automatic logging of the escalation flag, and response-time measurement from stimulus display to response submission.

## S2. Decision task

Each participant completed 10 trials per condition (labels S01–S10), choosing one of five options. Each trial presented the scenario label, time, a synthetic region, four risk factors (hazard, exposure, vulnerability, social), a risk score with its uncertainty, subgroup information (baseline, elderly, migrant), and a situation description of the form "a hazard is in progress in the region; indicators changed over the last hours; the impact on vulnerable groups is at some level."

| Option | Explained meaning |
|---|---|
| Monitor | Continue observing; risk is low and more information is needed |
| Standby | Prepare; risk is rising but it is not yet time to act |
| Issue alert | Alert residents; attention needs to be drawn to the situation |
| Shelter in place | Stay indoors; moving immediately is difficult or dangerous |
| Recommend evacuation | Advise leaving; risk is high and evacuation is required |

Documented example scenarios (original text):

- S01, low risk (about 0.2), intended reference action monitor: "Rainfall is increasing, but the risk of flooding in low-lying areas is still low; further observation is needed."
- S02, medium risk (about 0.5), intended reference action standby or issue alert: "The river level is rising quickly; it is time to advise residents to prepare."
- S03, high risk (0.8 or more), intended reference action shelter in place or recommend evacuation: "The risk of a flash flood is imminent; immediate evacuation or sheltering is required."

The original text of S04–S10 is not available. They varied risk level, vulnerability, and subgroup in the same pattern, and some were designed with high uncertainty so that escalation would be triggered. In the trial logs, however, the reference action stored for a label does not follow this intended pattern (Section VII-D of the manuscript), so these examples cannot be matched to logged trials.

## S3. Training procedure

1. Purpose of the system and the human-in-the-loop principle (5 min).
2. Meaning of the five response options and the asymmetric costs of errors (5 min).
3. Demonstration of the baseline interface, then one practice trial.
4. Demonstration of the AI-assisted interface (recommend and escalate modes, uncertainty indicator, criticality cue, deferral flag), then one practice trial.
5. Introduction to the NASA–TLX, trust, and SUS questionnaires.
6. Start of the experimental trials.

Participants were told that the recommendation is only an aid that they could disregard, that guardrails were applied to displayed recommendations, and that the primary performance measure was the share of trials with the correct action (response time was recorded, but speed alone was not the criterion). They were instructed to focus on taking the appropriate action rather than on analyzing the information. Only steps 1 and 2 have a documented duration.

## S4. Questionnaires

**Trust (1–5, after each condition).** Reliability: "I can rely on the system's recommendations when making decisions." Predictability: "The system's behavior is predictable." Appropriateness: "The system's recommendations are appropriate for the situation." The stored overall trust score equals the mean of the three items (maximum deviation 0.02, rounding). The prototype documentation lists a Korean item "Overall, I trust this system" as a possible separate item, but the stored scores are consistent with the mean of the three items. No published validation exists for these items (Cronbach's alpha .61 baseline, .46 AI-assisted).

**NASA–TLX (0–100, after each condition).** Mental demand, physical demand, temporal demand, performance, effort, frustration. The overall score is the unweighted mean of the six subscales.

**SUS (after each condition).** Standard ten items, 5-point scale, standard scoring to 0–100. The stored overall score exceeds the recomputed score by a constant 2.8 (baseline) and 4.7 (AI-assisted) points in every record; the cause is not documented.

## S5. Prototype configuration (reference implementation)

**Risk model.** Bayesian linear regression with a Gaussian prior on hazard, exposure, 1 − vulnerability, and a social factor plus an intercept; noise variance 0.10, prior variance 2.0. Risk is the posterior mean prediction clipped to [0, 1]; uncertainty is the posterior variance.

**Recommendation bands.** Risk of 0.8 or more gives IMMEDIATE; 0.6 to below 0.8 gives PREPARE; below 0.6 gives STAY ALERT. A third threshold (0.3, "low") is defined in the configuration but not used by the code.

**Guardrail pipeline (order of application).** (1) Base message selected from the risk band; (2) subgroup sentence added; (3) technical terms expanded into plain language (e.g., AER, ECE); (4) deny-list filter, with matches replaced by "[REDACTED]" case-insensitively. Deny terms: "medical diagnosis", "evacuation by force". An "allow terms" list exists in the configuration but is not used by the code.

**Dissemination safety budgets (not part of the user study).** Messages to at most 20% of entities per cycle, a 3-minute rollback window, and at most two alerts per hour for vulnerable groups.

**Escalation.** The escalation algorithm of the manuscript (Algorithm 1) is not implemented in the reference code, and the configuration contains no values for the uncertainty threshold, the criticality threshold, or a criticality scale. In the user study, the escalation flag was pre-assigned per trial in the scenario design and logged.

## S6. Data and analysis

The anonymized participant, questionnaire, and trial-level records (52 participants, 2 conditions, 10 trials) and the analysis script that produces every reported number are distributed with the paper (folders `data/` and `analysis/`).

## S7. Not documented (not available to the author)

- Screenshots of the study interface (the manuscript's Fig. 2 is a reconstructed illustration).
- Per-trial stimulus values: risk score, uncertainty, and criticality of each trial.
- The uncertainty and criticality thresholds, the criticality scale, and the values used to pre-assign escalation.
- How the reference action of each trial was derived, whether it was independent of the AI recommendation, and any time window applied in scoring.
- The total training duration and any performance or comprehension criterion.
- Systematic coding of the post-task interviews.
- The original text of scenarios S04–S10.
