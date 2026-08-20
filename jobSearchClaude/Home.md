# Rah's Job Search Vault

Local documentation for the two-agent job-search pipeline that lives at `github.com/rahulrawat20022002/jobSearchClaude`. This vault is intentionally kept OUT of the git repo (see `.gitignore`) so it can hold private working notes without polluting the tracked history. Drop the vault into `~/Desktop/jobSearchClaude/jobSearchClaude/` and open the folder in Obsidian.

## Start here

- [[Pipeline Overview]] — one page picture of the whole system, with the diagram embedded
- [[Daily Workflow]] — what Rah actually does each morning

## The three actors

- [[01 Agent A - Cowork Drafting]] — cloud scheduled task that searches, scores, tailors and pushes drafts
- [[02 Agent B - OpenClaw Submission]] — Mac-side agent that submits platform native listings
- [[03 Rah Manual - Company Portals]] — everything that agents are forbidden to touch

## The rules

- [[CV Rules]] — every historical dated rule in date order, with links to their source digests
- [[19 August 2026 Rules]] — the ten new rules from the Ojas comparison, current authoritative shape
- [[Skills Buckets]] — the five bucket labels and what belongs in each

## The system

- [[Notion Schema]] — every column in data source `fd974369-40b2-48c5-b660-d15256c88f52`
- [[File Structure]] — repo layout, what each file does, where drafts land
- [[build_html.py Overview]] — the render pipeline, overflow ladder, language block

## When things break (playbooks)

- [[Playbook - Push from Cowork Blocked]] — proxy 403 on `git push`, the bundle workaround
- [[Playbook - 2 Page Cap Exceeded]] — `RuntimeError: CV PDF still 3 pages after full overflow ladder`
- [[Playbook - Notion CSV Drift]] — reconciliation surfaced a mismatch, Notion always wins
- [[Playbook - Render Toolchain Failed]] — weasyprint or python-docx import failed at STEP 0
