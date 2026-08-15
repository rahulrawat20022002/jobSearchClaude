"""Runner for the 8 August 2026 job search run (top 4, normal cut, backlog 0)."""

from role_configs_08aug import CONFIGS_08AUG
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_08AUG:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
