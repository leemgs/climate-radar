from __future__ import annotations
from pathlib import Path
def main():
    print(Path("results/metrics.json").read_text())
if __name__ == "__main__":
    main()
