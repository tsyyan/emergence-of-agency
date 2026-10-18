# Bootstrap validation record

## Locally executed

Windows 11, Python 3.14.6, pinned upstream Buddie installed from requirements.
`python -m unittest discover -s tests -v`: **13 tests, OK** after review fixes.
`python -m agency check results/E000-bootstrap`: **5/5 expected control outcomes**.
`python -m agency check results/E000-versioned`: **5/5 expected control outcomes**.
Each bundle contains the real control subprocess outputs and Buddie receipts.
The initial bundle precedes the source commit; the second records source commit
`c2c8f9856dbb6007766d6da5a1e4269c0806e28a`. Historical evidence was not rewritten.

## Fresh code review

A separate reviewer inspected the spec, plan, source, tests and CI and ran the then-current
11 tests. Two substantive issues were reproduced and fixed with failing-then-passing regressions:

- Final receipt verdict edits were accepted when subject digest and overall PASS stayed unchanged.
  Compare all substantive fields, excluding only recheck time and historical locations.
  Regression: `test_changed_final_receipt_anchor_verdict_rejected`.
- Git LF normalization would change Windows receipt bytes and break recorded hashes.
  Preserve `results/**` bytes with `-text` and verify a real Git index/export round trip.
  Regression: `test_evidence_bytes_survive_git_checkout`.

The complete 13-test suite passed after both fixes. A separate relocation test had already
exposed and fixed comparison of absolute subject paths. No second reviewer pass is claimed.

Deferred minor: unexpected Buddie exit/no-receipt diagnostics are included in the raised error
but not saved as a separate failed-process record in the partial bundle. This affects debugging,
not successful-run validation. Partial directories remain preserved; CI retains step output.

## Decisions and limits

- Use the dedicated clone of an empty repository instead of a linked worktree: no initial
  commit existed from which to create a worktree. This affects workspace organization only.
- Use upstream CLI/file anchors, without a new Codex transcript adapter or MCP deployment.
  This limits verified claims to file evidence in E000; it avoids fabricating execution events.
- Publish initial main under the user's advance authorization; no existing branch history is replaced.
- Neither local logs nor receipts independently authenticate the author. Hosted CI is an
  additional execution record; green controls still do not establish agency or general accuracy.

The upstream full-suite failures are documented separately in `repository-audit.md`.
