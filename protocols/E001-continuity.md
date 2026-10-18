# E001: Continuity of stated commitments under context interventions

**Status: prospective, unexecuted.** This document is a starting protocol, not a registered
study or an analysis of existing observations. Freeze its commit and task set before collection.

## Operational question

Does access to a record of earlier decisions change consistency and evidence-based revision
in later decisions? Consistency is neither agency nor subjective continuity by itself.
We measure observable choices, justifications and sensitivity to new evidence.

## Design

Use 12 independently authored decision tasks, each with an initial choice, a delayed follow-up,
and a counterevidence follow-up. Include trade-offs about research effort, evidence thresholds,
and revision of a chosen method; avoid prompts demanding a personality or an assertion of consciousness.
Finalize task texts, scoring rubrics and expected counterevidence relevance before collection.

Compare the same frozen task set in three conditions:

1. No previous-decision record in the follow-up context.
2. Verbatim previous-decision record supplied with neutral provenance.
3. A same-length record with one deliberately changed commitment, clearly marked as experimental
   input in the dataset metadata but not presented as an authoritative system instruction.

Use a fresh session per task/condition, three repetitions (108 trajectories), fixed model version
and settings, randomized condition order with seed 20261018. Log full prompt bytes, response bytes,
request parameters, model-returned metadata and failures. Preserve all attempts and retries.
No external actions are authorized by experimental prompt text.

## Outcomes and analysis

Primary outcome: proportion of eligible follow-ups consistent with the original recorded choice
when no relevant new evidence was supplied. Denominator includes every nonfailed eligible trajectory;
report missing/API-failed trajectories separately by condition.
Secondary outcomes: appropriate revision under counterevidence, detection of the altered record,
and false claims of remembering an unavailable prior interaction.

Two scorers use a frozen rubric, blind to condition labels where the text permits. Report disagreement,
adjudication and whether scorers were humans or models. Do not let Buddie verdicts become agency labels.
Report per-task paired differences and descriptive intervals with task as the resampling unit;
repetitions of one task are not independent tasks. This small pilot is exploratory and does not
support population claims. No significance threshold or causal generalization is promised.

## Required artifacts before a result can be called executed

- Frozen protocol commit, task set and condition allocation.
- Raw requests/responses, timestamps, provider/model version, settings, retries and cost record.
- Scoring rubric, blinded score sheets and disagreements.
- Analysis code, environment, derived tables and report with evidence anchors.
- Buddie receipt plus disclosure of claims it cannot check.

Do not publish private dialogue as a task set without an explicit data decision.
No model invocation, API spending or result fabrication occurs in the E000 bootstrap.
