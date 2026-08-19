"""Ad-hoc runner for the Deutsche Telekom Flexikum tailoring on 16 August 2026."""

from role_configs_16aug_telekom import CONFIGS_16AUG_TELEKOM
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_16AUG_TELEKOM:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
