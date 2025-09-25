# Climate Radar

<p align="center">
  <img src=climate-radar-logo.png" alt="Climate RADAR Logo" width="150" height="150">
</p>


As climate-related hazards intensify worldwide, conventional early warning systems (EWS) remain effective at rapid alert dissemination but often fail to ensure that warnings translate into timely and effective protective actions. This persistent *alert–action gap* continues to drive preventable casualties, inefficient resource allocation, and inequities among vulnerable populations.

We present **Climate RADAR** (*Risk-Aware, Dynamic, and Action-Recommendation system*), a generative AI–driven reliability layer that reimagines disaster communication — shifting the focus from **alerts delivered** to **actions executed**. Climate RADAR integrates meteorological, hydrological, vulnerability, and social indicators into a **composite risk index** with full uncertainty propagation. Built on large language models (LLMs) equipped with robust guardrails — including policy filters, evidence attribution, confidence scoring, and human-in-the-loop escalation — the system personalizes recommendations for diverse stakeholders through multiple interfaces: a citizen mobile app, a volunteer coordination portal, a municipal command dashboard, and an accessibility-optimized chatbot.

We validate Climate RADAR across simulations, a controlled user study (*n* = 52), and a municipal pilot deployment. Results demonstrate significant improvements over conventional approaches: a **+37.5% increase** in protective action execution (*Cohen’s d* = 0.84, *p* < 0.01), **response latency halved** (18.2 → 9.7 minutes), a **17.5-point reduction** in cognitive workload (NASA-TLX), and a **+14.4-point gain** in usability (SUS). In real-world municipal operations, deployment further reduced volunteer duplication by **26%** and improved staff trust ratings (Likert mean **4.4/5**).

Our contributions are fourfold:

1. We introduce **action execution rate** as a primary reliability metric for early warning systems.
2. We formalize a **composite risk index** tightly integrated with guardrail-embedded LLMs.
3. We demonstrate **subgroup-aware fairness auditing** and **accountability logging** in a disaster response context.
4. We release the complete implementation — including source code, synthetic datasets, and evaluation scripts — as **open source** at [https://github.com/leemgs/climate-radar](https://github.com/leemgs/climate-radar).

By bridging predictive analytics, behavioral science, and responsible AI, Climate RADAR advances the vision of **self-healing reliability engines** for climate resilience. It operationalizes global priorities — such as the **Sendai Framework** and the **EU AI Act** — by enabling people-centered, equitable, and transparent early warning systems. In doing so, Climate RADAR contributes both the theoretical underpinnings and practical pathways needed to build next-generation, compliance-ready disaster resilience infrastructures.

---

### ✨ Key Improvements Made

* **Stronger narrative flow:** Opened with a clear problem → solution → validation → impact.
* **More concise technical phrasing:** Reduced redundancy (“fails to ensure that alerts translate…” → “often fail to ensure…”).
* **Improved readability:** Shorter sentences, clear transitions, and consistent verb tenses.
* **Enhanced clarity of contributions:** Reformatted into a numbered list for easier scanning.
* **Polished academic tone:** Better suited for journal abstracts, executive summaries, or funding proposals.

---


# Reproducible Reference Implementation

This repository provides a lightweight, **fully reproducible** reference implementation of the *Climate RADAR* pipeline:
synthetic data generation, Bayesian-style composite risk modeling with uncertainty, guardrailed recommendation synthesis,
safety-budgeted orchestration, fairness auditing, audit logging, and figure/metric generation — all **offline**.

## Quickstart

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make reproduce
```

Artifacts will appear under `results/` (metrics + figures) and `audit/sample_log.jsonl`.

## Make targets
- `make reproduce` : end-to-end
- `make data`      : regenerate synthetic data
- `make fit`       : fit composite risk model
- `make recs`      : generate recommendations (guardrails + safety budgets)
- `make eval`      : compute AER, EOD (elderly/migrant), ECE
- `make figures`   : save plots (histogram + calibration)

## Docker
```bash
docker build -t climate-radar -f docker/Dockerfile .
docker run --rm -v $PWD:/app climate-radar make reproduce
```

> Educational reference; not for real-world emergency use.
