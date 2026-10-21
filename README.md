# TneenVoice Studio

Local voice cloning and dialect TTS for Windows — **Somali** and **Egyptian Arabic** first-class, plus multilingual OmniVoice.

**Author:** Ahmed Elsayed  
**Download (Windows):** [https://voicestudio.tneen.cloud](https://voicestudio.tneen.cloud)

## Highlights

- Desktop app with automatic local backend on launch
- **Somali cloning** → OmniVoice + Somali orthography when you attach a reference; **Somali TTS** → Meta MMS Somali when not cloning
- **Egyptian Arabic** → Lahgtna OmniVoice fine-tune (cloning supported when installed)
- Recording guide shows what to say for a strong clone reference (Somali / Egyptian / more)
- Existing Hugging Face / app caches are reused (same Windows app id `com.voicestudio.desktop`)

## License

AGPL-3.0. Based on [VoiceStudio / OmniVoice](https://github.com/debpalash/VoiceStudio). Model weights have separate licences (see Model Catalogue).

## Install from source

```powershell
bun install
bun run desktop
```

Windows installer build:

```powershell
bun run --cwd electron dist -- --win --x64
```

See [docs/install/tneenvoice-windows.md](docs/install/tneenvoice-windows.md).
