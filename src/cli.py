from __future__ import annotations
import argparse, subprocess, sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["reproduce","data","fit","recs","eval","figures"])
    args = ap.parse_args()
    if args.cmd == "reproduce":
        subprocess.check_call(["make","reproduce"])
    else:
        subprocess.check_call(["make", args.cmd])
if __name__ == "__main__":
    main()
