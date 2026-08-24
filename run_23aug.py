"""Runner for the 23 August 2026 scheduled Cowork run (top 4, normal cap)."""

from role_configs_23aug import CONFIGS_23AUG
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_23AUG:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
