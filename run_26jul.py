"""Runner for the 26 July 2026 job search run (top 10, normal cut)."""

from role_configs_26jul import CONFIGS_26JUL
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_26JUL:
        try:
            build_role(cfg)
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
