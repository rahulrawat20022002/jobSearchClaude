"""Runner for the 24 August 2026 scheduled job search run (top 3, capped cut)."""

from role_configs_24aug import CONFIGS_24AUG
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_24AUG:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
