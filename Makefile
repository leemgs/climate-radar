PY?=python

.PHONY: reproduce data fit recs eval figures clean

reproduce: data fit recs eval figures

data:
	$(PY) -m src.data.generate_synthetic --out data/synthetic

fit:
	$(PY) -m src.reproducibility.pipeline fit

recs:
	$(PY) -m src.reproducibility.pipeline recs

eval:
	$(PY) -m src.reproducibility.pipeline eval

figures:
	$(PY) -m src.reproducibility.pipeline figures

clean:
	rm -rf results/* audit/sample_log.jsonl
