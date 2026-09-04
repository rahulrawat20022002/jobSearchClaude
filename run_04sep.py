"""Runner for the 4 September 2026 ad hoc single-role draft (Beilmann Marketing)."""

from role_configs_04sep import CONFIGS_04SEP
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_04SEP:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
