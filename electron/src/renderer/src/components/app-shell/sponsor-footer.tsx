import { useNavigate } from '@tanstack/react-router';
import { BlocksIcon } from 'lucide-react';
import { useTranslation } from 'react-i18next';
import { runRendererTask } from '@/lib/global-error-recovery';
import { SITE_URL } from '@shared/utils/contactLinks';
import { getBridge } from '@/components/bridge';
import './sponsor-footer.css';

/** Product footer: integrations + site — no upstream sponsor/repo chrome. */
export function SponsorFooter() {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const openSite = () => {
    const bridge = getBridge();
    void runRendererTask('Open TneenVoice site', () =>
      bridge?.files?.openExternal?.(SITE_URL) ?? Promise.resolve(),
    );
  };

  return (
    <div className="sponsor-footer-host">
      <footer aria-label={t('integrationCatalog.title')} className="sponsor-strip">
        <button
          type="button"
          className="sponsor-footer-action"
          onClick={() =>
            runRendererTask('Open integrations', () => navigate({ to: '/integrations' }))
          }
        >
          <BlocksIcon aria-hidden="true" className="size-4" />
          <span>{t('integrationCatalog.title')}</span>
        </button>
        <button type="button" className="sponsor-footer-action" onClick={openSite}>
          <span>voicestudio.tneen.cloud</span>
        </button>
      </footer>
    </div>
  );
}
