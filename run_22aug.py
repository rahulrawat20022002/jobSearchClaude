"""Runner for the 22 August 2026 job search run (top 3, normal cut)."""

from role_configs_22aug import CONFIGS_22AUG
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_22AUG:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
