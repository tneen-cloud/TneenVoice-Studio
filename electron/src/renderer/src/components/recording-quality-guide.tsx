import { useTranslation } from 'react-i18next';
import scripts from '@/lib/recording-scripts.json';
import { languageCode } from '@/lib/language-options';

type ScriptEntry = { tipsKey: string; script: string };

const TABLE = scripts as Record<string, ScriptEntry>;

function entryForLanguage(language?: string | null): ScriptEntry {
  const code = language ? languageCode(language) || language.toLowerCase() : '';
  if (code && TABLE[code]) return TABLE[code];
  const lower = (language || '').toLowerCase();
  if (lower.includes('somali')) return TABLE.so;
  if (lower.includes('egyptian')) return TABLE.arz;
  if (lower === 'arabic' || lower.includes('arabic')) return TABLE.ar;
  if (lower.includes('english')) return TABLE.en;
  return TABLE.default;
}

/** Shown while cloning: what to say for a strong reference in the chosen language. */
export function RecordingQualityGuide({ language }: { language?: string | null }) {
  const { t } = useTranslation();
  const entry = entryForLanguage(language);
  return (
    <aside
      className="rounded-lg border border-border/60 bg-muted/40 p-3 text-sm text-muted-foreground"
      aria-label={t('clone.recordGuide.title')}
    >
      <p className="mb-1 font-medium text-foreground">{t('clone.recordGuide.title')}</p>
      <p className="mb-2">{t(entry.tipsKey)}</p>
      <p className="mb-1 text-xs uppercase tracking-wide">{t('clone.recordGuide.readAloud')}</p>
      <blockquote className="rounded-md bg-background/80 p-2 font-medium text-foreground leading-relaxed">
        {entry.script}
      </blockquote>
    </aside>
  );
}
