"""Runner for the 5 Fraunhofer thesis listings Rah asked for ad hoc on 25 August 2026."""

from role_configs_fraunhofer import CONFIGS_FRAUNHOFER
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_FRAUNHOFER:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
