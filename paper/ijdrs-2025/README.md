# From Alerts to Actions: Climate RADAR as a Generative AI–Driven Reliability Layer for Disaster Resilience

## 📘 Journal Submission
**Submitted to:** *International Journal of Disaster Risk Science (IJDRS, SCIE)*
**Status:** Under peer review
**Submission date:** 2025-10-16
**Category:** Generative AI / Disaster Resilience / Responsible AI Systems

> This is a different paper from the IEEE THMS manuscript in [`../thms-2026/`](../thms-2026/). The figures below are those reported in the IJDRS submission and are not the results of the THMS manuscript.

## 📄 PDF
The submitted PDF was removed from the repository. It remains in the git history:
[ijdrs_sn_jnl_climate_radar_20251016_1610.pdf (commit 369cc2a)](https://github.com/leemgs/climate-radar/blob/369cc2a8e13e9c6ec74050131660d2805e6ea1a3/paper/ijdrs_sn_jnl_climate_radar_20251016_1610.pdf)

## 🔑 Keywords
Early Warning Systems (EWS) · Disaster Resilience · Generative AI · Responsible AI · Composite Risk Index · Human-Centered Response

## 🧩 Abstract
As climate-related hazards intensify, conventional early warning systems (EWS) disseminate alerts rapidly but often fail to trigger timely protective actions, leading to preventable losses and inequities.
We introduce **Climate RADAR (Risk-Aware, Dynamic, and Action Recommendation system)**, a **generative AI–based reliability layer** that reframes disaster communication from alerts delivered to actions executed.

The system integrates meteorological, hydrological, vulnerability, and social data into a **composite risk index** and employs **guardrail-embedded large language models (LLMs)** to deliver personalized recommendations across citizen, volunteer, and municipal interfaces.

Evaluation through simulations, user studies, and a municipal pilot demonstrates improved outcomes, including higher protective action execution, reduced response latency, and increased usability and trust.
By combining **predictive analytics, behavioral science, and responsible AI**, Climate RADAR advances **people-centered, transparent, and equitable early warning systems**, offering practical pathways toward compliance-ready disaster resilience infrastructures.

## Extended summary (as written for the IJDRS submission)
As climate-related hazards intensify worldwide, conventional early warning systems (EWS) remain effective at rapid alert dissemination but often fail to ensure that warnings translate into timely and effective protective actions. This persistent *alert–action gap* continues to drive preventable casualties, inefficient resource allocation, and inequities among vulnerable populations.

Climate RADAR integrates meteorological, hydrological, vulnerability, and social indicators into a composite risk index with full uncertainty propagation. Built on LLMs equipped with guardrails (policy filters, evidence attribution, confidence scoring, and human-in-the-loop escalation), the system personalizes recommendations for diverse stakeholders through a citizen mobile app, a volunteer coordination portal, a municipal command dashboard, and an accessibility-optimized chatbot.

The IJDRS submission reports validation across simulations, a controlled user study (*n* = 52), and a municipal pilot deployment: a +37.5% increase in protective action execution (Cohen's *d* = 0.84, *p* < 0.01), response latency halved (18.2 → 9.7 minutes), a 17.5-point reduction in cognitive workload (NASA-TLX), a +14.4-point gain in usability (SUS), 26% less volunteer duplication, and staff trust ratings of 4.4/5 in municipal operations.

Contributions stated in the submission:
1. **Action execution rate** as a primary reliability metric for early warning systems.
2. A **composite risk index** integrated with guardrail-embedded LLMs.
3. **Subgroup-aware fairness auditing** and **accountability logging** in a disaster response context.
4. An open-source reference implementation with synthetic data and evaluation scripts (see [`../../code/`](../../code/)).

## 🧾 Citation (BibTeX)
```bibtex
@article{lim2025climateradar,
  title     = {From Alerts to Actions: Climate RADAR as a Generative AI–Driven Reliability Layer for Disaster Resilience},
  author    = {Lim, Geunsik},
  journal   = {International Journal of Disaster Risk Science},
  year      = {2025},
  note      = {Under peer review, submitted October 16, 2025},
  keywords  = {Generative AI, Disaster Resilience, Responsible AI, Early Warning Systems, Composite Risk Index}
}
```
