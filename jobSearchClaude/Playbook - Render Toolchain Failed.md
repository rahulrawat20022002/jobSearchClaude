# Playbook — Render Toolchain Failed

## Symptom

[[01 Agent A - Cowork Drafting]] STEP 0 fails during environment preflight. Either `pip install weasyprint python-docx --break-system-packages` errors, or the `python3 -c "import weasyprint, docx"` check raises `ModuleNotFoundError` / an ImportError from a missing system library (typically Cairo, Pango, or GObject on the weasyprint side).

## The forbidden fix

Never fall back to markdown-only output. The rule dates to the CoverLetter PDF requirement (11 August 2026, see [[CV Rules]]) and the failure philosophy in [[01 Agent A - Cowork Drafting]].

Shipping `.md` only and burying the failure in Notes is a rule violation of the same weight as flipping a Notion row to `applied` without verifying (invariant #3, [[Pipeline Overview]]). Silent downgrades to a lesser deliverable are forbidden.

## The correct fix

HALT the run. Do not proceed past STEP 0. Draft the Gmail digest with a `render toolchain failed` transparency block:

```
Job Digest YYYY-MM-DD — HALTED at STEP 0

Preflight failure: weasyprint import failed with <full traceback>.

No roles drafted this run. Backlog unchanged. Reconciliation not run
(reconciliation depends on the checkout being usable and requires the
data source query which STEP 0 gates).

Next steps:
- Inspect the sandbox base image / pinned pip index for the missing
  system dependency.
- Re-run once the toolchain installs cleanly.
```

The digest still lands in Gmail Drafts, so Rah sees what happened at his normal morning check per [[Daily Workflow]].

Send a Cowork notification with the same summary so Rah does not have to check email to know the run failed.

## Common root causes and where to look

### weasyprint fails to import with `OSError: no library called ...`

Weasyprint depends on system Cairo, Pango and GObject libraries. In a fresh sandbox these may not be pre-installed.

Debug:

```
apt list --installed 2>/dev/null | grep -E 'cairo|pango|glib'
```

Fix in the sandbox base:

```
apt-get update && apt-get install -y libcairo2 libpango-1.0-0 libpangoft2-1.0-0 libgdk-pixbuf2.0-0 libffi-dev
```

Then re-run `pip install weasyprint --break-system-packages`.

### `pip install` times out or fails with 403

The sandbox proxy may not allow-list pypi. Similar territory to [[Playbook - Push from Cowork Blocked]] but on a different domain (pypi.org vs github.com).

Debug:

```
curl -I https://pypi.org
```

If curl fails too, the proxy is the cause. This is not something Agent A can fix at run time; halt and notify.

### python-docx imports but a docx render silently fails

`python-docx` sometimes imports successfully but breaks at write time if `CV_Template.docx` is missing or has been corrupted. Check:

```
python3 -c "from docx import Document; Document('/tmp/JobSearch/CV_Template.docx')"
```

If this fails, the template file is the cause, not the library. Restore from a known-good commit.

### pypdf import fails

`pypdf` is used in the overflow ladder to count pages (see [[build_html.py Overview]] "The overflow ladder"). If it is missing:

```
pip install pypdf --break-system-packages
```

Halt-report if the install fails; the ladder cannot run without page counting.

## Do NOT

- Do NOT patch `render_role()` to skip PDF generation "just for today".
- Do NOT wrap the import in a try/except and fall through with a warning.
- Do NOT ship the 4 markdown files as the deliverable set and claim STEP 5 as successful.
- Do NOT mark rows as `drafted` in Notion when only markdown rendered. If they are marked drafted, [[02 Agent B - OpenClaw Submission]] will try to upload PDFs that do not exist on its next run and halt in a much more expensive way.

## When the toolchain is chronically flaky

If STEP 0 fails on 2+ consecutive scheduled runs, escalate to Rah — the base image or the sandbox provisioning has drifted and needs pinning rather than fixing per-run. Draft a summary of the last three failure tracebacks in the digest so Rah has data to work with.

## See also

- [[01 Agent A - Cowork Drafting]] STEP 0 for the preflight itself
- [[01 Agent A - Cowork Drafting]] "Failure philosophy" for why HONESTY over throughput
- [[CV Rules]] "11 August 2026 — CoverLetter PDF required" for the historical reason PDFs are non-negotiable
