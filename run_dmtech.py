"""Runner for the dmTECH GmbH JobTeaser listing Rah asked for ad hoc on 25 August 2026.

SS Engineers entries are hidden for this role per Rah's request, via an
in process override of build_html.SHOW_SS_ENGINEERS_EXPERIENCE. This does
not change the on disk default (True) for any other role or future run.
"""

import build_html
from role_configs_dmtech import CONFIGS_DMTECH

if __name__ == "__main__":
    build_html.SHOW_SS_ENGINEERS_EXPERIENCE = False
    for cfg in CONFIGS_DMTECH:
        try:
            build_html.build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
