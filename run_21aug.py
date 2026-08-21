"""Runner for the 21 August 2026 job search run (top 3, normal cut)."""

from role_configs_21aug import CONFIGS_21AUG
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_21AUG:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
