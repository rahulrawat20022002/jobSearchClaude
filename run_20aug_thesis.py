"""Runner for the 20 August 2026 Amprion Masterarbeit initiative."""

from role_configs_20aug_thesis import CONFIGS_20AUG_THESIS
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_20AUG_THESIS:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
