from services.language_engine import preferred_tts_backend_for_language, resolve_tts_backend_id
from services.somali_text import normalize_somali_for_tts, looks_mostly_english
from services.egyptian_text import normalize_egyptian_for_tts


def test_language_prefs():
    assert preferred_tts_backend_for_language("Somali") == "mms-somali"
    assert preferred_tts_backend_for_language("Somali", wants_cloning=True) == "omnivoice"
    assert preferred_tts_backend_for_language("Egyptian Arabic") == "egyptian-omnivoice"
    assert preferred_tts_backend_for_language("English") is None


def test_explicit_engine_wins(monkeypatch):
    assert resolve_tts_backend_id(language="Somali", explicit_engine="omnivoice", active_engine="voxcpm2") == "omnivoice"


def test_somali_digits_and_markers():
    assert "kow" in normalize_somali_for_tts("1 cunto")
    assert looks_mostly_english("This is for you and the team")


def test_egyptian_strips_tashkeel():
    # fatha on alef should disappear
    raw = "أَهلا"
    out = normalize_egyptian_for_tts(raw)
    assert "\u064e" not in out
