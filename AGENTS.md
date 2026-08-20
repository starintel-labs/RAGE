# RAGE Research Agent Instructions

This file is authoritative for humans and automated agents working in this repository.

## Before changing anything

Observe, do not assume:

```bash
git status --short
git branch --show-current
git remote -v
find .. -name AGENTS.md -print
```

Read every applicable nested `AGENTS.md`. Do not overwrite unrelated work. Current source, tests, scripts, and tracked repository state override stale prose or remembered behavior.

## RAGE

RAGE means **Recursive Analysis with Gated Execution**.

Every loop must be grounded in observed state. Analysis identifies evidence, constraints, contradictions, and unknowns. Execution is admitted only by an explicit gate. Evaluation records what actually happened. The next loop starts from that evidence rather than from the previous plan.

Do not treat a plan, generated patch, existing file, merge, or green build as proof that a gate was approved.

## Repository model

- `roam/research/` owns research and findings.
- `roam/design/` owns canonical designs.
- `roam/implement/` owns active implementation working copies.
- `roam/indexes/` owns project indexes and roadmaps.
- `scripts/` owns capture, lifecycle, synchronization, and validation.
- `tests/` owns regression coverage for repository mechanics.
- `skills/` owns phase-specific agent procedures.

Use existing scripts before inventing parallel workflow machinery.

## Skills

Inspect `skills/README.md` and the frontmatter of relevant `skills/*/SKILL.md` files before beginning a non-trivial task.

Use the smallest applicable skill set. Do not bulk-load every skill into context.

- Use `rage-loop` when the task spans a complete RAGE cycle.
- Use `rage-research` for evidence gathering and research-note work.
- Use `rage-gate` when deciding whether a state transition is admitted.
- Use `rage-execute` only after the active gate is open.
- Use `rage-evaluate` to verify observed results against the gate.
- Use `rage-recurse` to derive the next loop, repair path, or termination state.

When several phases are required, apply them in this order:

```text
rage-research -> rage-gate -> rage-execute -> rage-evaluate -> rage-recurse
```

`rage-loop` may coordinate those phase skills but does not weaken their preconditions. Skills refine this file; they never override repository authority, permissions, required evidence, or observed state.

## Document contract

Every substantive Org document must contain:

```org
:PROPERTIES:
:ID: stable-id
:END:
#+title:
#+description:
#+status:
#+filetags:
```

It must also contain an approval table and changelog.

Use this approval header:

```org
* Approval Table

| Approval area | Required authority | State | Evidence required | Evidence reference |
|---------------+--------------------+-------+-------------------+--------------------|
```

Allowed approval states are `PENDING`, `NOT STARTED`, `APPROVED`, `REJECTED`, `SUPERSEDED`, and `NOT APPLICABLE`.

Never fabricate approval or evidence. `NOT APPLICABLE` needs a reason. Preserve stable IDs. Duplicate IDs and unresolved `id:` links are validation failures.

Use this changelog header:

```org
* Changelog

| Date | Change | Author or actor | Evidence |
|------+--------+-----------------+----------|
```

Research must separate verified facts, inference, contradictions, and unresolved questions. For externally changing facts, prefer current primary sources and record retrieval dates.

## Implementation gates

Each immediate project subtree under `roam/implement/` may contain at most one active Org design.

Promote through `scripts/implement.py`; do not manually create competing active copies. Record terminal outcomes through `scripts/mark-design.py`. Implemented and rejected ledgers are append-only evidence.

Retries and repeated runs must be idempotent where practical. A stale or failed run must not silently become success.

## Generated and sensitive material

Do not commit `.cache/`, `_site/`, generated databases, credentials, authorization headers, private evidence, session material, or secrets.

Never hand-edit generated output. Change source or generators instead.

## Validation

Before completion run and observe:

```bash
git diff --check
git diff --stat
python3 -m py_compile scripts/*.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/sync.py
python3 scripts/sync.py --check
python3 scripts/validate-docs.py
```

Never claim a command passed unless it was executed and its result was observed. Never bypass a failing wrapper with a lower-level command just to obtain a green exit code.
