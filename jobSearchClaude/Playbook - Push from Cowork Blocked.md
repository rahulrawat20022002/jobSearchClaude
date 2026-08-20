# Playbook — Push from Cowork Blocked

## Symptom

At [[01 Agent A - Cowork Drafting]] STEP 8, `git push origin main` fails from the Cowork sandbox with an HTTP 403 or a "proxy blocked" error, or hangs on connect. This happens when a Cowork interactive session hits a proxy allowlist that does not include `github.com`. Scheduled task runs (which authenticate with a PAT baked into the prompt) typically go through and are not affected.

## Confirm it is this problem, not something else

- `git remote -v` shows the correct `https://...@github.com/rahulrawat20022002/jobSearchClaude.git`.
- `git status` shows a clean working tree with the target commit already made locally.
- `git log -1` matches the commit you expect to push.
- `git push origin main` returns `fatal: unable to access ... 403` OR blocks and eventually times out.
- A parallel `curl -I https://github.com` from the same shell also fails or is refused.

If `git status` is dirty or `git log -1` is the wrong commit, this is not the playbook — go back and fix the commit first.

## The bundle workaround

A git bundle is a single-file transport of one or more commits. Cowork can hand Rah the bundle via SendUserFile; Rah applies it on his Mac (which has normal GitHub access) and pushes from there. Same commit content, same commit hash, just a different network path.

### From the Cowork sandbox

```
cd /tmp/JobSearch
git bundle create /tmp/YYYYMMDD_docs.bundle origin/main..HEAD
```

`origin/main..HEAD` means "every commit reachable from HEAD that is NOT already on origin/main" — exactly the commits Cowork would have pushed. Deliver the bundle via SendUserFile, then notify.

### On Rah's Mac

```
cd ~/Desktop/jobSearchClaude
git fetch /path/to/downloaded/YYYYMMDD_docs.bundle main:cowork_incoming
git merge --ff-only cowork_incoming
git branch -d cowork_incoming
git push origin main
```

- `git fetch` reads the bundle as if it were a remote and lands its commits on a local branch `cowork_incoming`.
- `git merge --ff-only` fast-forwards `main` to that branch. Fails cleanly if a fast-forward is not possible, which is what you want: it means Rah has committed something on the Mac since Cowork last synced, and the two branches diverged.
- Delete the transient branch, then push to GitHub normally.

## When a fast-forward fails

Means the Mac has diverged from the bundle. Options:

1. `git log --oneline main..cowork_incoming` — see what the bundle adds.
2. `git log --oneline cowork_incoming..main` — see what the Mac added that the bundle does not have.
3. Decide: rebase Cowork's commits on top of Mac (`git rebase main cowork_incoming` then `merge --ff-only`), or the reverse. Rarely, a merge commit is more honest than either rebase; in that case `git merge cowork_incoming` and resolve conflicts.

Do NOT `git push --force` in any of these paths. Cowork does not force push per [[01 Agent A - Cowork Drafting]] STEP 8, and Rah should match that discipline.

## When it happens vs when it does not

- **Interactive Cowork sessions:** commonly blocked. The interactive proxy is stricter about arbitrary outbound HTTPS.
- **Scheduled task Cowork runs:** usually go through when the run uses a PAT injected via the prompt env, because scheduled runs use a different network path with the PAT already authenticated to github.com.
- **Rah's Mac:** always fine; the Mac has full outbound access.

If a scheduled task also fails to push, that is unusual and worth investigating rather than immediately falling back to the bundle — the PAT may have expired or the repo path may have moved.

## Historical precedent

- **19 August 2026:** the CV rewrite commit (`8048186 19 Aug 2026 CV rewrite`) was made in a Cowork interactive session, could not push, delivered as `cv_rewrite_19aug.bundle`. Rah applied on Mac and pushed.
- **20 August 2026:** the .gitignore + Obsidian docs commit was made in a scheduled task run. Push succeeded (if this playbook is being read, that path was clear; otherwise the run would have delivered a bundle the same way).

## See also

- [[01 Agent A - Cowork Drafting]] STEP 8 for the push step itself
- [[Daily Workflow]] "What NOT to do" for the concurrent-push trap
