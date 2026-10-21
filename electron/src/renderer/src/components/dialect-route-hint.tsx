import { languageCode } from '@/lib/language-options';
import { useCloneSetting } from '@/lib/store/clone-settings';
import { useReference } from '@/lib/store/reference';
import { useTranslation } from 'react-i18next';

/** Surfaces which dialect engine will be used for the selected language. */
export function DialectRouteHint() {
  const { t } = useTranslation();
  const language = useCloneSetting('language');
  const profile = useReference((s) => s.profile);
  const file = useReference((s) => s.file);
  const code = language ? languageCode(language) || language.toLowerCase() : '';
  const lower = (language || '').toLowerCase();
  const cloning = Boolean(profile || file);

  let message: string | null = null;
  if (code === 'so' || lower.includes('somali')) {
    message = cloning
      ? t('clone.dialectRoute.somaliClone')
      : t('clone.dialectRoute.somaliTts');
  } else if (code === 'arz' || lower.includes('egyptian')) {
    message = t('clone.dialectRoute.egyptian');
  }

  if (!message) return null;

  return (
    <p
      className="mb-2 rounded-md border border-primary/25 bg-primary/5 px-3 py-2 text-sm text-foreground"
      role="status"
    >
      {message}
    </p>
  );
}
