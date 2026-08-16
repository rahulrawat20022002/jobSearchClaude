"""Runner for the 16 August 2026 scheduled run (top 3, soft cap gate)."""

from role_configs_16aug import CONFIGS_16AUG
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_16AUG:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
