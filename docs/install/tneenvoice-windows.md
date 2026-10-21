# TneenVoice Studio — Windows install

1. Download the installer from [voicestudio.tneen.cloud](https://voicestudio.tneen.cloud).
2. Run the NSIS setup (current user by default). Start Menu entry: **TneenVoice Studio**.
3. On launch the app starts the local backend automatically.

## Models you already have

The app keeps the same Windows app id and data folders as VoiceStudio, so
existing downloads under `%LOCALAPPDATA%\OmniVoice\hf_cache` and the managed
runtime under `%APPDATA%\VoiceStudio` are reused. New dialect engines only
download when you first need them and they are missing.

## Languages

TneenVoice Studio supports **all** languages the engines provide (multilingual
cloning and TTS). Somali and Egyptian Arabic get dedicated routing when you
select them:

- **Somali** (clone) → OmniVoice + orthography; (TTS only) → MMS Somali when installed.
- **Egyptian Arabic** → Lahgtna Egyptian OmniVoice when installed.
