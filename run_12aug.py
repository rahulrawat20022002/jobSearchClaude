"""Runner for the 12 August 2026 job search run (top 5, normal cut, backlog 3)."""

from role_configs_12aug import CONFIGS_12AUG
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_12AUG:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
