from __future__ import annotations
from typing import List, Dict

def sanitize(text: str, deny_terms: List[str]) -> str:
    low = text.lower()
    for t in deny_terms:
        if t.lower() in low:
            text = text.replace(t, "[REDACTED]")
    return text

def glossary_expand(text: str, glossary: List[Dict[str,str]]) -> str:
    out = text
    for g in glossary:
        term, plain = g.get("term"), g.get("plain")
        out = out.replace(term, f"{term} ({plain})")
    return out
