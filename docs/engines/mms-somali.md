# TneenVoice Studio — MMS Somali Engine

MMS Somali loads Meta's [`facebook/mms-tts-som`](https://huggingface.co/facebook/mms-tts-som)
VITS checkpoint — a Somali-trained text-to-speech model from the Massively
Multilingual Speech project. Use it when you need **fluent Somali reading**.
It does **not** clone a reference voice.

## When to pick it

- Somali scripts, announcements, classroom demos, and local-language UI reads.
- Any time OmniVoice / VoxCPM2 produce English-leaning Somali.

Trade-off against [OmniVoice](omnivoice.md): Somali-only, fixed speaker, no
cloning — but natural Somali pronunciation instead of a weak accent guess.

## Setup

1. Install **facebook/mms-tts-som** from **Model Catalogue** (TTS tab), or let
   the first generate download it from Hugging Face.
2. Select the engine via **Settings → Engines → MMS Somali**, or set
   `OMNIVOICE_TTS_BACKEND=mms-somali`.
3. Set language to **Somali** and generate.

## Model selection

| Variable | Default | Meaning |
| --- | --- | --- |
| `OMNIVOICE_MMS_SOMALI_MODEL` | `facebook/mms-tts-som` | Hugging Face checkpoint |

## Behaviour notes

- Output is typically **16 kHz** mono (from the VITS config).
- Runs on **CUDA** when available, otherwise **CPU** (model is ~36M params).
- Non-Somali `language` values are rejected; leave language as Somali / `so`.
- Reference audio and instruct prompts are ignored (no cloning).
- Weights are **CC-BY-NC 4.0** — fine for university / non-commercial demos;
  do not redistribute the model commercially.

## Attribution

Please credit Meta's MMS project when you publish results that use this
engine. See the [model card](https://huggingface.co/facebook/mms-tts-som).
