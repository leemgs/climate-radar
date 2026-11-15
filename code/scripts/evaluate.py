from __future__ import annotations
from pathlib import Path

RESULTS = Path(__file__).resolve().parents[2] / "artifact" / "results"


def main():
    print((RESULTS / "metrics.json").read_text())


if __name__ == "__main__":
    main()
