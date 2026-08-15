"""Runner for the 23 July 2026 job search run (top 5, backlog soft cap)."""

from role_configs_23jul import CONFIGS_23JUL
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_23JUL:
        try:
            build_role(cfg)
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
