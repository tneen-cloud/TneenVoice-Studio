# TneenVoice Studio design system

Surface branding for the TneenVoice Studio fork of VoiceStudio (AGPL-3.0).
Upstream application IDs and runtime paths are unchanged; only the visible brand,
colours, and assets diverge here.

## Brand

| Token | Value |
|-------|--------|
| Product name | **TneenVoice Studio** |
| Mark | Stylised **T** with a horizontal voice-wave bar (see `electron/public/favicon.svg`) |
| Artwork | Blue signal field (`electron/public/signal-field.webp`) |
| Upstream credit | Based on [VoiceStudio / OmniVoice](https://github.com/debpalash/VoiceStudio) (AGPL-3.0) |

## Colour

Canonical CSS lives in `electron/src/renderer/src/styles/t3-theme.css`, bridged to
Tailwind via `globals.css` (`--color-primary` → `var(--primary)`).

| Role | Light | Dark | Notes |
|------|-------|------|--------|
| Primary | `oklch(0.52 0.17 252)` | `oklch(0.68 0.14 252)` | Clear blue (hue ~252), not violet |
| Primary foreground | white | white | On solid CTAs |
| Ring / focus | `--primary` | theme focus | Matches primary |
| Update accent | `--primary` | blue-tinted | Inherits primary |
| Success / warning / error | emerald / amber / red | same family | Unchanged semantic colours |
| Surfaces | zinc / white | neutral-950 | Neutral chrome; colour comes from primary actions |

Named Settings palettes (`t3-palettes.ts`) still override `--primary` when the
user picks a non-default theme. The default (no `data-theme-id`) is TneenVoice blue.

## Radius and type

- `--radius: 0.625rem` — shared control corner radius.
- UI copy uses the existing app type stack (Inter / system via shell CSS).
- Prefer `t('…')` i18n keys; never hardcode brand strings outside locales and
  `config/app.json`.

## Logo usage

- Prefer the SVG mark at 16–32px for chrome; full artwork for empty states / sidebar.
- Do not place detached badges or glow stickers over the mark.
- Keep sufficient contrast on both light and dark backgrounds.

## Mobile parity

After editing theme CSS or `t3-palettes.ts`, regenerate tokens:

```sh
bun scripts/export-mobile-tokens.ts
```

That updates `mobile/contract/tokens.json` and the iOS/Android generated token files.
