# TneenVoice Studio — Windows install

1. Download the installer from [voicestudio.tneen.cloud](https://voicestudio.tneen.cloud).
2. Run the NSIS setup (current user by default). Start Menu entry: **TneenVoice Studio**.
3. On launch the app starts the local backend automatically.

## Models you already have

The app keeps the same Windows app id and data folders as VoiceStudio, so
existing downloads under `%LOCALAPPDATA%\OmniVoice\hf_cache` and the managed
runtime under `%APPDATA%\VoiceStudio` are reused. New dialect engines only
download when you first need them and they are missing.

## Somali / Egyptian

- **Somali** → MMS Somali engine (auto when language is Somali).
- **Egyptian Arabic** → Lahgtna Egyptian OmniVoice when installed.
