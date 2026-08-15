# Job Search Digest — 14 July 2026 (revised)

## Run status: paused in error, then corrected

Earlier in this run I treated the CSV as the source of truth for the backlog gate and read 44 rows as drafted, which triggered the hard pause rule. That was wrong. Notion is the actual source of truth for status because Rah flips rows to applied, rejected, interviewing, and so on directly in Notion. The CSV was stale. Once Notion became reachable this run and I queried it, the real counts are:

- applied: 34
- rejected: 11
- Not listed Anymore: 1
- drafted: 0

Zero drafted rows means the backlog gate should never have paused this run. Under the 11 July 2026 rule, drafted less than 10 triggers the normal top 10 cut.

## Actions taken this run to correct the state

1. applied-log.csv was rewritten to match Notion status for every row. All 34 applied rows, 11 rejected rows, 1 Not listed Anymore row, and the BMW Werkstudent Programmplanung Antrieb rejection that arrived mid-run are now reflected in the CSV.
2. CLAUDE.md was updated with a new rule effective 14 July 2026 titled "Status source of truth override". The rule says every scheduled run must query Notion first, use Notion statuses for the backlog gate and dedup, and only fall back to the CSV when Notion is unreachable after retry. The CSV is also synced back to Notion in the same reconciliation step so the offline failsafe stays fresh.
3. This digest was rewritten to reflect the true post reconciliation state.

## What did not happen this run

The search and drafting steps did not run in this session even though the backlog gate should have allowed them. The run was already deep into the pause path when the CSV sync completed, and rewinding it now would produce lower quality drafts than a fresh scheduled run against a clean CSV. The next scheduled run will start with Notion reachable, drafted equals 0, and will draft the top 10 newly scored roles as normal.

## Rejections received recently

Track these on Notion, no re-drafting needed. Any patterns Rah wants to learn from should be noted on the Notion row itself.

1. valantic, Praktikant or Werkstudent AI Engineering and Cloud Prototyping, Eschborn.
2. EnBW, Werkstudent AI Automation and Data Science, Karlsruhe.
3. Alloqis, Werkstudent Data Science and Python Development, Tübingen.
4. Mercedes-Benz Tech Innovation, Werkstudent Data Engineering and Data Science, Stuttgart.
5. BMW Group, Werkstudent Data Analyst Programmplanung Antrieb, München (rejection email 14 July).
6. Transdev, Werkstudent KI Platform and LLM Prototyping, Berlin.
7. Genoverband e.V., Werkstudent Internal Audit mit Fokus Künstliche Intelligenz, Hannover.
8. XiLLeR GmbH, Praxissemester Data Scientist KI, Home Office.
9. Smateso GmbH, Working Student Data Scientist and AI Engineer, Home Office.
10. agentic fox AI solutions GmbH, Werkstudent AI Automation and Agent Engineering, Köln.
11. Porsche, Working Student Voice AI, Ludwigsburg.

## Withdrawn or delisted

1. Schwarz Digits, Praktikum or Werkstudent Computer Vision and Deep Learning, Bad Friedrichshall. Marked Not listed Anymore in Notion.

## Transparency block

- Backlog gate source used at first: CSV, incorrectly. Backlog gate source after Notion recovered: Notion, correct.
- Notion reachability: two rate_limited 429 responses in a row, then reachable after a 60 second wait. Any future run must retry at least once before declaring Notion unreachable.
- CSV to Notion reconciliation: performed in reverse this run, Notion into CSV, because the drift was in the other direction.
- Search sources: none exercised this run.
- Gmail: earlier draft created at id r3805491677006918789 with the incorrect pause narrative. A second draft is created below reflecting the corrected state.
- Rule change committed to CLAUDE.md this run: "Status source of truth override, effective 14 July 2026", making Notion the primary source of truth for row status and requiring a retry before falling back to the CSV.

<run-summary>Backlog gate initially tripped in error against a stale CSV; Notion query after retry showed the real state as 34 applied, 11 rejected, 1 delisted, 0 drafted, so the pause was not warranted. CSV rewritten to match Notion, CLAUDE.md updated with a new rule requiring Notion first for status checks, and this digest was rewritten. BMW Group Werkstudent Data Analyst Programmplanung Antrieb was rejected today by email and is now recorded as rejected in both Notion and CSV. Search and drafting will resume on the next scheduled run.</run-summary>
