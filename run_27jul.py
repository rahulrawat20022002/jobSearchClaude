"""Runner for the 27 July 2026 job search run (top 5, soft backlog cap)."""

from role_configs_27jul import CONFIGS_27JUL
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_27JUL:
        try:
            build_role(cfg)
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
