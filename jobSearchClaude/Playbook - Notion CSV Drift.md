# Playbook — Notion CSV Drift

## Symptom

[[01 Agent A - Cowork Drafting]] STEP 3 (reconciliation) surfaces one or more rows where Notion's `Status` disagrees with `applied-log.csv`'s `Status` for the same `Company + Role`, OR a row appears in one system that does not exist in the other.

## Invariant

Notion is the source of truth for row status (shared invariant #1, see [[Pipeline Overview]], set by the 14 July 2026 rule in [[CV Rules]]). The CSV is a mirror only. When the two disagree, the CSV is wrong, not Notion.

Consequences:

- Status disagreement → CSV updated to match Notion.
- CSV row exists but Notion row does not exist → Agent A creates the Notion row using the CSV status. This is the ONLY case where the CSV informs a Notion write on reconciliation, and it is not really "drift resolution"; it is filling a missing row.
- Notion row exists but CSV row does not exist → Agent A appends the row to the CSV using the Notion status. Notion wins here too.

Never the reverse: CSV never overrides a live Notion row's status.

## The reconciliation step in detail

For each row in `applied-log.csv`:

1. Compute the match key: `(Company.lower().strip(), Role.lower().strip())`.
2. Look up the same key in Notion (query the data source, filter by Company property).
3. If Notion has the row and `Status` differs → update the CSV row's `Status` to Notion's value. Log the change to the digest's transparency block.
4. If Notion does not have the row → create it with `Status = <CSV status>`, `Date Drafted = <CSV date>` if present, `Draft Path = <CSV path>` if present. Log as `created in Notion from CSV`.

Then in the reverse direction, for each Notion row where `Status = drafted`:

5. If the CSV does not have a matching row → append it. Log as `appended to CSV from Notion`.

Rows with `Status != drafted` in Notion but missing from CSV are logged but NOT auto-appended, since those are typically old rows Rah cleaned out of the CSV intentionally.

## When to intervene manually

- **A drift that has re-appeared multiple runs in a row.** Reconciliation should be idempotent — after one run, the CSV should match Notion. If drift reappears the next day for the same row, that means something (Rah, or an unexpected script) is re-writing the CSV between runs. Investigate before letting reconciliation keep patching over it.
- **A drift where Notion looks wrong to Rah.** The invariant says Notion wins, but the invariant assumes Notion reflects reality. If Rah accidentally clicked `applied` on a row that was never submitted, fix Notion first, then let reconciliation propagate. Never fix the CSV directly.
- **A drift involving Status values that neither system recognises.** Notion's `Status` select is fixed (see [[Notion Schema]]). If the CSV has `Status = pending` or some other unrecognised value, Notion cannot mirror it. Reconcile by deciding the correct Notion value first (probably `drafted`), then updating the CSV.

## The 11 July 2026 rule: reconciliation runs on paused runs too

Even when the [[01 Agent A - Cowork Drafting]] STEP 2 backlog gate says pause (11+ drafted), STEP 3 still runs. This catches drift on quiet days when no drafting happens. Do not skip reconciliation to save time.

## What the digest transparency block should say

After a reconciliation run, the day's `Job_Digest_YYYY-MM-DD.md` transparency block should include:

```
Reconciliation:
- N rows checked
- M drift(s) resolved (CSV updated to Notion)
- K rows appended to CSV from Notion (missing before this run)
- J rows created in Notion from CSV (missing before this run)
```

If any of M / K / J is nonzero, the specific `Company + Role` and the direction of the fix should be listed below.

Silent reconciliation is a rule violation per invariant #5 (report exactly what happened, see [[Pipeline Overview]]). Even a run with zero drift should print `Reconciliation: 0 drifts, N rows checked`.

## Order of operations traps

- Do not edit `applied-log.csv` directly to "fix drift". Fix in Notion, let reconciliation propagate.
- Do not run reconciliation manually as a one-off outside of [[01 Agent A - Cowork Drafting]]. It should always run in the context of a full agent run so the digest captures what changed.
- Do not delete rows from the CSV to "clean up". If they are gone from Notion first, reconciliation will not re-add them (the reverse-direction step only adds `Status = drafted` Notion rows). If they are still in Notion, they will re-appear next reconciliation.

## See also

- [[Notion Schema]] for the exact column names and values
- [[01 Agent A - Cowork Drafting]] STEP 3 for the step itself
- [[CV Rules]] 14 July 2026 (source of truth rule) and 11 July 2026 (paused runs rule)
