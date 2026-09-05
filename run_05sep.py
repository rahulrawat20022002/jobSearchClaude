"""Runner for the 5 September 2026 scheduled job search run (normal top 3 cut)."""

from role_configs_05sep import CONFIGS_05SEP
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_05SEP:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
