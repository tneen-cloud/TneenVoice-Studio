"""Map output language → preferred TTS engine (TneenVoice dialect routing).

Only recommends an engine when that engine is available. Never forces a
download mid-generation. An explicit per-request ``engine`` override wins.
"""
from __future__ import annotations

from typing import Optional


def _normalize_lang(language: object) -> Optional[str]:
    if language is None:
        return None
    if not isinstance(language, str):
        return None
    value = language.strip().lower()
    if not value or value == "auto":
        return None
    try:
        from omnivoice.utils.lang_map import LANG_NAME_TO_ID

        if value in LANG_NAME_TO_ID:
            return LANG_NAME_TO_ID[value]
    except Exception:
        pass
    aliases = {
        "egyptian arabic": "arz",
        "egyptian": "arz",
        "masri": "arz",
        "somali": "so",
        "arabic": "ar",
        "standard arabic": "ar",
    }
    if value in aliases:
        return aliases[value]
    head = value.replace("_", "-").split("-", 1)[0]
    if head.isascii() and head.isalpha() and len(head) in (2, 3):
        return head
    return value


def preferred_tts_backend_for_language(
    language: object,
    *,
    wants_cloning: bool = False,
) -> Optional[str]:
    """Return an engine id to prefer for ``language``, or None.

    Somali MMS is fluent TTS but cannot clone. When the caller has a
    reference clip / profile (``wants_cloning``), prefer OmniVoice so Somali
    orthography + voice cloning still work; otherwise prefer MMS Somali.
    Egyptian Lahgtna supports cloning when weights are present.
    """
    code = _normalize_lang(language)
    if code == "so":
        return "omnivoice" if wants_cloning else "mms-somali"
    if code == "arz":
        return "egyptian-omnivoice"
    return None


def resolve_tts_backend_id(
    *,
    language: object = None,
    explicit_engine: Optional[str] = None,
    active_engine: Optional[str] = None,
    wants_cloning: bool = False,
) -> str:
    """Pick the engine for a generate call.

    Order: explicit request → language preference (if available) → active.
    """
    from services import tts_backend as tts

    if explicit_engine and str(explicit_engine).strip():
        return str(explicit_engine).strip()

    preferred = preferred_tts_backend_for_language(language, wants_cloning=wants_cloning)
    if preferred:
        try:
            cls = tts.get_backend_class(preferred)
            ok, _ = cls.is_available()
            if ok:
                # For egyptian-omnivoice, also require weights when we can tell.
                if preferred == "egyptian-omnivoice":
                    if getattr(cls, "weights_ready", lambda: True)():
                        return preferred
                else:
                    return preferred
        except Exception:
            pass

    return (active_engine or tts.active_backend_id() or "omnivoice").strip()
