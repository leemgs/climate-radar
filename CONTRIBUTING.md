# Contributing
- Papers go in `paper/<venue>-<year>/` (see `paper/README.md`); code in `code/`; generated outputs in `artifact/`.
- Keep modules small, pure (numpy/pandas/matplotlib only).
- No network calls; offline determinism.
- Seed any randomized component.
- `make reproduce` (run in `code/`) must pass locally.
