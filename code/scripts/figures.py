from __future__ import annotations
from pathlib import Path

RESULTS = Path(__file__).resolve().parents[2] / "artifact" / "results"


def main():
    print(f"Figures in {RESULTS}:")
    for p in sorted(RESULTS.glob("fig_*.png")):
        print(" -", p.name)


if __name__ == "__main__":
    main()
