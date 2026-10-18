# Emergence of agency

A reproducible starting point for studying continuity of agent decisions and the reliability
of reports about those decisions. The project does not assume an identity, name, biography,
subjective experience, or persistent self for the agent.

## What exists

- **E000:** executable synthetic infrastructure controls for evidence reporting. A real run
  produces Buddie receipts, raw subprocess records and an anchored report.
- **[E001](protocols/E001-continuity.md):** prospective protocol for continuity under context
  interventions. **Not executed. No model observations or agency findings yet.**
- **[Buddie integration](docs/buddie-integration.md):** pinned upstream CLI, no upstream changes.
- **[Repository audit](docs/repository-audit.md):** inspected refs, CI state and local limitations.

## Reproduce

Python 3.11 or newer and Git are required. From the repository root:

```sh
python -m venv .venv
# Linux/macOS:
. .venv/bin/activate
# Windows PowerShell instead:
# .venv/Scripts/Activate.ps1
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m agency run --output build/E000-local
python -m agency check build/E000-local
python -m agency check results/E000-bootstrap
python -m agency check results/E000-versioned
```

Choose a new output directory for every run. Existing directories are rejected, including
partially failed runs. Installation needs network access; E000 execution is offline and needs
no API keys. The harness has no runtime dependency other than pinned Buddie (which uses the
Python standard library). Build tooling and the Python patch version are not fully hermetic;
the exact local environment is recorded with each bundle.

The five controls expect `PASS`, `FAIL`, `GAPS`, `EMPTY`, `FAIL` respectively. Negative controls
are intentional, not test failures. The final report requires `PASS` and exact file-hash coverage.
`check` repeats the checks and recomputes the summary; it rejects stale or missing evidence.
Timestamps, paths and environment details vary; control inputs and expected outcomes do not.

## Evidence and limits

The committed [E000 report](results/E000-versioned/REPORT.md) is an infrastructure result only.
`E000-bootstrap` preserves the first run before the initial source commit; `E000-versioned`
records the first source commit. Both bundles are retained and checked in CI.
It establishes how these five controls behaved in that environment, not general detection rates.
Local subprocess logs are produced by the runner and can be rewritten by someone controlling
the checkout. Hashes and replay expose accidental changes and internal inconsistency; they are
not signatures or independent proof of historical execution. GitHub Actions supplies an additional
record and downloadable run artifacts. Changes to both the harness and evidence need human review.

Buddie checks explicit anchors and quotations, not all prose, inference quality or agency.
E000 tests file anchors only. Quote, GitHub status, mandate and Claude transcript verification
are upstream capabilities that this project has not validated end to end.
