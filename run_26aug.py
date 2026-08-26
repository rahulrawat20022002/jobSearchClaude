"""Runner for the 26 August 2026 scheduled job search run (top 4, normal cut)."""

from role_configs_26aug import CONFIGS_26AUG
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_26AUG:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
