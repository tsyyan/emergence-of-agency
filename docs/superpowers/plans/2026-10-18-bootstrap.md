# Research bootstrap implementation plan

> Execute inline with superpowers:executing-plans; the user requested autonomous work.

**Goal:** Publish a reproducible control run and independent Buddie integration.
**Architecture:** stdlib runner calls pinned Buddie CLI, saves raw outputs and receipts, and replays evidence.
**Tech stack:** Python >=3.11, unittest, GitHub Actions.
**Spec:** ../specs/2026-10-18-bootstrap-design.md

## Global constraints
- Buddie stays unchanged; pin ddb4db85496a1889d2ea8768a7841eb60d9353e9.
- E000 is infrastructure only; E001 has no model observations yet.
- New output directories only, UTF-8 and LF artifacts, no fabricated session transcripts.

## Review focus
- GAPS and EMPTY must not pass the strict final-report gate.
- Hashes must work across Windows and Linux checkouts.
- Missing evidence and altered metrics must fail replay.
- Historical paths/timestamps must not be compared as deterministic scientific outcomes.
- CI and local records establish execution only within their trust boundary.

## Task 1: Evidence runner and gate
Files: agency/__main__.py, agency/controls.py, tests/test_controls.py.
Interfaces: run(output: Path), check(output: Path), strict_report(report: Path, required: list[Path]).
- [ ] Write real subprocess integration tests for five controls, replay, refusal to overwrite,
      tampering, missing receipt and strict coverage failures; observe failure before implementation.
- [ ] Implement controls and replay, preserving raw CLI receipts and command outputs.
- [ ] Run `python -m unittest discover -s tests -v`; require no failures.
- [ ] Run `python -m agency run --output results/E000-bootstrap` then check that directory.
- [ ] Commit implementation and actual evidence.

## Task 2: Research protocol, documentation, CI
Files: README.md, AGENTS.md, protocols/E001-continuity.md, docs/buddie-integration.md,
docs/repository-audit.md, .github/workflows/research.yml.
- [ ] Document observed upstream state, trust limits, reproduction and unexecuted protocol.
- [ ] Add cross-platform CI with artifact upload and committed evidence replay.
- [ ] Obtain fresh whole-project review; fix substantive issues with regression tests.
- [ ] Push authorized initial main, observe workflow completion and artifact availability.
