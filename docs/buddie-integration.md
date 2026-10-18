# Minimal independent Buddie integration

## Selected interface

Use `python -m buddie verify REPORT --repo DIR --no-fetch --no-github --json RECEIPT`.
`requirements.txt` pins public main at `ddb4db85496a1889d2ea8768a7841eb60d9353e9`.
No changes, releases, issues, or configuration writes are made in tsyyan/buddie.
The CLI is sufficient for local use and CI; no server or connector deployment is necessary.

The runner creates five actual subprocess calls, retaining their argv, return code, output,
timestamps and in-toto receipts. It does not serialize these as Claude Code session events.
Buddie's `run:` verification currently trusts Claude's transcript format. Codex compatibility
would require a separately designed adapter and a clear provenance boundary; it is not part of
this bootstrap. File anchors work without that adapter.

## Acceptance policy belongs here

Upstream's exit status is 1 only for FAIL. GAPS and EMPTY exit 0. `strict_report` requires:

1. zero return code and receipt outcome PASS;
2. at least one expected artifact;
3. exact equality between expected file-hash anchors and held anchors.

Replay checks the fixed control reports, fixture bytes, observed/expected outcomes, saved
report digests, exit codes, derived summary, deterministic final report and its receipt subject.
The final report covers all control reports, receipts, execution records, environment and summary.
Absolute paths inside historical receipts are retained as evidence, never used to resolve replay.
The final receipt is compared in full except for recheck time, subject name and anchor repo paths.
`results/** -text` preserves raw receipt bytes through Git checkout, including Windows CRLF.

Receipts are ordinary JSON, not cryptographically signed attestations. The author can rewrite
all mutually consistent files; this integration does not prevent that. CI runs the same harness
from a checkout and uploads its own bundle. The workflow uses read-only repository permissions,
no model API secrets, and no privileged pull_request_target event.

## Optional interactive use

Upstream also exposes an MCP stdio service via `python -m buddie serve` with `verify_report`,
`snap` and `source_text`. This is a documented next option, not an installed Codex connector.
No new Claude hook is installed. To verify cited sources in future research, retain lawful
snapshots and run the quote checker with a defined source-access policy; E000 does not test it.

Known minor limitation: an unexpected Buddie process failure before a receipt exists raises an
error with stdout/stderr, but does not save that failed process record in the partial bundle.
The partial directory is retained and cannot be overwritten; CI retains step diagnostics.

## Upgrade

Review upstream diff from the current pin, edit the full SHA in requirements and `agency.controls.PIN`,
reinstall, run tests and a fresh control bundle, and compare outcomes. Preserve old evidence.
Do not silently follow lab-sync or main. Upstream's export-from-lab workflow is its own concern.
