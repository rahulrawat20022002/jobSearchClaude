# Playbook — 2 Page Cap Exceeded

## Symptom

`render_role()` in `build_html.py` raises:

```
RuntimeError: CV PDF for [folder] still 3 pages after full overflow ladder
    (19 Aug 2026 hard 2 page cap). Steps tried: [(...), (...), ...].
    Tighten the profile paragraph in the config or drop a certificate for this role.
```

This is rule 6 of [[19 August 2026 Rules]] being enforced. Halting a role is the correct behaviour per invariant #3 (never fabricate an outcome, see [[Pipeline Overview]]); a false success would be a 3-page CV shipped anyway.

## Confirm which rung the ladder exhausted at

The `Steps tried: [(...)]` list in the RuntimeError message enumerates every rung the ladder tried and the page count after each. Read the last entry: if it is the densest rung (`projects_kept=1, pp_bullets=1, ss_ft=1, ss_intern=1, eray=1, certs_kept=1, research_kept=1`) and page count is still 3, the profile paragraph or the header itself is the fat.

If the ladder stopped earlier because pages dropped BUT some intermediate step went back up, that is a sign the overflow ladder has a monotonicity bug — file that separately, not part of this playbook.

## The three usual causes

### 1. Profile paragraph too long

The profile paragraph (first block under the header) is not part of the ladder. If it runs past ~4 lines it silently eats the second-page real estate the ladder is trying to preserve.

**Fix:** shorten `cfg['profile']` for this role. Target 3 lines in the rendered PDF. Keep the strongest positioning claim, cut the softer supporting sentence.

### 2. Too many certifications

Certifications are trimmed by the ladder but only from the tail. If Rah has 6 certs and the ladder trims to 1, the render still spends 1 line on the certifications heading and 1 on the remaining cert. When most rungs still leave 4 to 5 certs, they eat space.

**Fix:** drop a certification for this role via `cfg['certifications'] = [...][:N]` where N is the number that fits comfortably. Prefer keeping the most role-relevant certs.

### 3. Long eRay bullets

The eRay bullets themselves are trimmed by count but a single very long bullet can wrap to 4+ lines and defeat the count-based ladder. The 19 Aug 2026 rule 1 (no hyphens) and rule 2 (no parentheses in bullets) both help here — they typically make bullets shorter, not longer, once rewritten.

**Fix:** shorten the offending bullet in `role_configs.py` (or its per-day override). Target 2 lines per bullet in the rendered PDF.

## Order of operations for the fix

1. Read the failing role's `cfg` in the day's `role_configs_YYYYMMDD.py`.
2. Read the profile paragraph. If it wraps past 4 lines in the failing PDF, tighten it. Re-run just this role via `sample_cv_render.py` or a one-off invocation of `render_role(cfg)`.
3. If profile is fine, drop one certification. Re-run.
4. If still failing, look at the eRay bullets rendered from the tail of the ladder rungs. Shorten the longest one.
5. Re-run STEP 5 for this role only. If it passes, commit the config change with a message like `role_configs_YYYYMMDD.py: tighten profile for [Company_Role] to fit 2 pages`.
6. Do NOT change the ladder itself to accommodate one role. The ladder is calibrated across the whole queue; loosening it means every future role gets a laxer cap.

## When to just drop the role

If a role cannot be tailored to 2 pages without cutting content Rah would want to keep, that is a signal the role is a poor fit and the CV would not read well anyway. Options:

- Flip the Notion row to `withdrawn` with Notes reason `2-page cap not achievable without stripping core positioning`.
- OR keep it drafted for manual submission where Rah wants to hand-edit the CV. Note this in Notes.

Never ship a 3 page CV under a config change that turns the cap off. Rule 6 is a hard cap, not a soft target.

## Debugging aid

To see how many pages the current defaults produce for a role WITHOUT triggering the ladder, patch `render_role` temporarily to log `pages` at each rung. The `tried` list already captured in the RuntimeError message is your best diagnostic — read it before running anything.

## See also

- [[19 August 2026 Rules]] rule 6 for the cap itself
- [[build_html.py Overview]] "The overflow ladder" for the rung sequence
- [[CV Rules]] "4 August 2026 — CV three page hard cap (SUPERSEDED)" for the historical context
