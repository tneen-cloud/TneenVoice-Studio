# TneenVoice Studio — Egyptian OmniVoice

Uses the Lahgtna Egyptian fine-tune of OmniVoice
(`ehabnegm/lahgtna-omnivoice-egyptian-v3`) for **Egyptian Arabic (arz)**.

## When it is used

Selecting language **Egyptian Arabic** auto-routes generation to this engine
when the checkpoint is already in your Hugging Face cache / Model Catalogue.
Your default `k2-fsa/OmniVoice` weights are never deleted.

## Tips

- Feed **raw Egyptian** text — avoid MSA diacritics on colloquial lines.
- Install the catalogue entry once; later launches reuse the cache.
