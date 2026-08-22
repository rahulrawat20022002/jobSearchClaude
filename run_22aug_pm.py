"""Runner for the 22 August 2026 afternoon supplemental run (2 more AI Engineer drafts)."""

from role_configs_22aug_pm import CONFIGS_22AUG_PM
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_22AUG_PM:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
