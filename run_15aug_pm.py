"""Runner for the 15 August 2026 afternoon scheduled run (top 3, normal cut)."""

from role_configs_15aug_pm import CONFIGS_15AUG_PM
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_15AUG_PM:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
