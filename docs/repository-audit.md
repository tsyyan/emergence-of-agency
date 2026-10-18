# Repository audit — 2026-10-18

Inspected via GitHub repository metadata, remote clone, branches, workflow runs and source files.

## emergence-of-agency

Public, default branch main, initially empty (no commits, code, workflows or results).
Implementation uses a dedicated new clone because an unborn branch cannot have a linked worktree.
The synced ChatGPT project `sources/` directory was not changed.
The prior chat reader returned user requests but assistant messages were unresolved content references;
no missing assistant research or decisions were reconstructed as memories.

## buddie

Public, main `ddb4db85496a1889d2ea8768a7841eb60d9353e9` (merge of lab-sync PR #3).
Python >=3.11, no core runtime dependencies. Packages: `buddie/` (anchors, effects, mandate,
CLI, MCP and hooks), `verbatim/` (quotes, numbers and source snapshots). Also `tests/`,
`examples/`, `skills/`, historical `results/`, provenance and licensing files.
README says this repository is exported from a separate lab; preserve that independence.

Main's observed CI [37150446692](https://github.com/tsyyan/buddie/actions/runs/37150446692)
is success. Latest observed run [37926560401](https://github.com/tsyyan/buddie/actions/runs/37926560401)
is failure on lab-sync `112d9222b43ee0af81b50f56228849fe367df6ed`: Ubuntu Python 3.13 failed
at apt-get installation before tests; the other Python jobs were cancelled, OS smoke jobs succeeded.
Do not confuse that failure with the pinned main's status.

Local full upstream suite on Windows/Python 3.14.6: **143 passed, 19 skipped, 11 failed**.
Failures: `tests/quotes/test_verbatim.py::test_access_jobs_keep_every_index_entry` (Windows snapshot
replace PermissionError); `tests/test_buddie.py::test_anchors` (fixture newline/hash mismatch);
and nine `tests/test_mandate.py` tests (locale-written fixture bytes read as UTF-8):
`test_verdicts_follow_the_plan`, `test_done_claims`, `test_auto_claim_is_recomputed`,
`test_anchored_queue_is_judged_at_its_commit`, `test_consent_needs_the_users_words_at_that_time`,
`test_partial_export_cannot_refute`, `test_next_step_names_its_row`, `test_queue_and_accepted`,
`test_receipt_and_hook`. These are baseline limitations, not fixed or hidden by this project.
E000 writes bytes explicitly as UTF-8/LF and sets UTF-8 for Buddie subprocess output.
The narrow integrated path is verified separately; a successful E000 is not an upstream suite pass.

No branches or files in Buddie were modified. No existing research claims in its README were
independently reproduced during this audit.
