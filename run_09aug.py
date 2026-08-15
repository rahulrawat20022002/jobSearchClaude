"""Runner for the 9 August 2026 job search run (top 4, normal cut, backlog 5)."""

from role_configs_09aug import CONFIGS_09AUG
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_09AUG:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
