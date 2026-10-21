# TneenVoice Studio

Fully local voice cloning, TTS, dubbing, and dictation for **every language** — on your Windows PC.

**Author:** Ahmed Elsayed  
**Download (Windows):** [https://voicestudio.tneen.cloud](https://voicestudio.tneen.cloud)

## Highlights

- Desktop app with automatic local backend on launch
- Multilingual cloning and synthesis (hundreds of languages via OmniVoice and companions)
- **Somali** and **Egyptian Arabic** get dedicated engine routing and recording guides (extras — not limits)
- Recording guide shows what to say for a strong clone reference in the selected language
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
