from __future__ import annotations
from pathlib import Path
def main():
    print("Figures in results/:")
    for p in Path("results").glob("fig_*.png"):
        print(" -", p.name)
if __name__ == "__main__":
    main()
