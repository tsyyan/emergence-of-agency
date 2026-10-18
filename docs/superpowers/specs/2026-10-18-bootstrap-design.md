# Reproducible research bootstrap

The user authorized independent implementation and publication in tsyyan/emergence-of-agency;
tsyyan/buddie remains an independent upstream and is not modified.

## Question and boundary
Can this project distinguish a valid artifact report from an altered, missing, or unanchored one?
E000 is an executed infrastructure control, not an experiment demonstrating agency or consciousness.
E001 is a prospective protocol about continuity of stated commitments under context interventions.
No language-model runs, credentials, fabricated transcripts, or claims of subjective continuity belong in E000.

## Alternatives
Use the upstream CLI (selected): small adapter, real receipts, no Buddie fork.
MCP would help interactive verification but adds deployment and has no advantage for offline CI.
Changing Buddie's transcript parser for Codex would couple projects and is unnecessary for file evidence.

## Components and contract
Python >=3.11; stdlib harness, Buddie pinned to full upstream main commit.
`python -m agency run --output DIR` creates a new output directory and never overwrites evidence.
Run real Buddie subprocesses on five controls: valid hash -> PASS, wrong hash -> FAIL,
missing file -> GAPS, no anchors -> EMPTY, malformed anchor -> FAIL.
Keep each report, receipt, command, exit code, stdout, stderr, UTC execution times,
Python/platform/git provenance, and input fixture bytes. Summarize actual observed outcomes.
Generate an anchored Markdown report. A strict local gate requires PASS and nonempty complete
file-hash coverage; upstream alone exits zero for GAPS and EMPTY.
`python -m agency check DIR` replays controls, compares recorded observations and derived summary,
and verifies the final report with Buddie. It must reject missing/changed files and altered metrics.
Receipts bind bytes, not truth or execution authenticity; logs are local subprocess records,
not signed attestations or Claude transcripts. CI provides an additional execution record.

## Verification
Test normal replay, overwrite refusal, tampered fixture, changed summary, missing receipt,
and strict rejection of empty, incomplete, and unavailable evidence. CI on Linux and Windows
installs pinned Buddie, runs tests, runs controls, checks both new and committed bundles,
and uploads artifacts even on failure. E001 remains explicitly unexecuted.
