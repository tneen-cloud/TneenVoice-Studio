"""MMS Somali engine: language gate + generate shape without loading HF weights."""
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest
import torch


@pytest.fixture
def tts():
    from services import tts_backend

    return tts_backend


def test_mms_somali_is_registered(tts):
    assert "mms-somali" in tts._REGISTRY
    cls = tts.get_backend_class("mms-somali")
    assert cls.id == "mms-somali"
    assert cls.supports_cloning is False
    assert cls().supported_languages == ["so"]


def test_mms_somali_rejects_english(tts):
    backend = tts.get_backend_class("mms-somali")()
    with pytest.raises(ValueError, match="Somali|so|mms-somali|MMS"):
        backend._check_language("English")


def test_mms_somali_generate_shape_with_mocked_model(tts):
    backend = tts.get_backend_class("mms-somali")()

    class _Tok:
        def __call__(self, text, return_tensors="pt"):
            assert text.strip()
            return {"input_ids": torch.ones(1, 4, dtype=torch.long)}

    class _Model:
        config = SimpleNamespace(sampling_rate=16000)

        def __call__(self, **_inputs):
            return SimpleNamespace(waveform=torch.zeros(1, 3200))

    backend._model = _Model()
    backend._tokenizer = _Tok()
    backend._sample_rate = 16000
    backend._device = "cpu"
    backend._ensure_loaded = lambda: None

    wav = backend.generate("Salaam calaykum", language="Somali")
    assert isinstance(wav, torch.Tensor)
    assert wav.ndim == 2
    assert wav.shape[0] == 1
    assert wav.shape[1] == 3200
    assert backend.sample_rate == 16000


def test_mms_somali_empty_text_raises(tts):
    backend = tts.get_backend_class("mms-somali")()
    backend._model = MagicMock()
    backend._tokenizer = MagicMock()
    with pytest.raises(tts.TTSInputError):
        backend.generate("   ", language="so")
