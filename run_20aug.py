"""Runner for the 20 August 2026 job search run (top 3, normal cut).

Backlog gate at run start: 0 drafted rows in Notion. Normal top 3 to 5
cut per 28 July 2026 yield reset. Reconciliation of 11 CSV rows to
Notion status ran before this pipeline invocation.
"""

from role_configs_20aug import CONFIGS_20AUG
from build_html import build_role


if __name__ == "__main__":
    for cfg in CONFIGS_20AUG:
        try:
            build_role(cfg)
            print(f"  OK: {cfg['folder']}")
        except Exception as e:
            print(f"  FAILED to build {cfg['folder']}: {e}")
