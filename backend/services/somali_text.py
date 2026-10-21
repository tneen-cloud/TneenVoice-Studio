"""Somali Latin orthography helpers for TTS.

Somali spelling is largely phonemic. Digraphs ``dh``, ``kh``, ``sh`` and
letters ``c`` (/ʕ/), ``x`` (/ħ/), ``q`` (/q/) must survive cleanup. Doubled
vowels mark length. See Somali Latin alphabet / Hooyo pronunciation notes.
"""
from __future__ import annotations

import re
import unicodedata

_DIGIT = {
    "0": "eber",
    "1": "kow",
    "2": "laba",
    "3": "saddex",
    "4": "afar",
    "5": "shan",
    "6": "lix",
    "7": "toddoba",
    "8": "siddeed",
    "9": "sagaal",
}

_ABBR = {
    "dr.": "doctor",
    "mr.": "mister",
    "mrs.": "missus",
    "etc.": "iww",
}


def normalize_somali_for_tts(text: str) -> str:
    """Prepare Somali Latin text for MMS / dialect TTS."""
    if not text:
        return ""
    out = unicodedata.normalize("NFC", text)
    out = out.replace("\u200b", "").replace("\ufeff", "")
    # Protect digraphs from aggressive letter cleanup (casefold carefully).
    for raw, repl in _ABBR.items():
        out = re.sub(re.escape(raw), repl, out, flags=re.IGNORECASE)

    def _digits(match: re.Match[str]) -> str:
        return " ".join(_DIGIT.get(ch, ch) for ch in match.group(0))

    out = re.sub(r"\d+", _digits, out)
    # Collapse whitespace; keep apostrophe (glottal) used in Somali.
    out = re.sub(r"[^\S\n]+", " ", out).strip()
    return out


def looks_mostly_english(text: str) -> bool:
    """Heuristic: Latin text with almost no Somali-typical letters."""
    letters = [c for c in text.lower() if c.isalpha()]
    if len(letters) < 8:
        return False
    somali_markers = sum(1 for c in letters if c in "cxq")
    digraphs = len(re.findall(r"dh|kh|sh", text.lower()))
    if somali_markers + digraphs > 0:
        return False
    return re.search(r"\b(the|and|is|you|for|this|that|with)\b", text.lower()) is not None
