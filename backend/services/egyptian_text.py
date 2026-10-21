"""Egyptian Arabic (arz) text prep for dialect TTS.

Egyptian fine-tunes (e.g. Lahgtna) want raw colloquial text — MSA tashkeel on
Masri often hurts pronunciation.
"""
from __future__ import annotations

import re
import unicodedata

# Arabic combining marks (tashkeel + Quranic marks commonly pasted).
_TASHKEEL = re.compile(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]")

_ARABIC_INDIC = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
_DIGIT_WORDS = {
    "0": "صفر",
    "1": "واحد",
    "2": "اتنين",
    "3": "تلاتة",
    "4": "أربعة",
    "5": "خمسة",
    "6": "ستة",
    "7": "سبعة",
    "8": "تمانية",
    "9": "تسعة",
}


def normalize_egyptian_for_tts(text: str) -> str:
    if not text:
        return ""
    out = unicodedata.normalize("NFC", text)
    out = _TASHKEEL.sub("", out)
    out = out.translate(_ARABIC_INDIC)

    def _digits(match: re.Match[str]) -> str:
        return " ".join(_DIGIT_WORDS.get(ch, ch) for ch in match.group(0))

    out = re.sub(r"\d+", _digits, out)
    out = re.sub(r"\s+", " ", out).strip()
    return out
