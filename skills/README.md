# RAGE Skills

Repo-local skills for agents operating the RAGE workflow.

Load only the skill needed for the current phase:

- `rage-loop` — orchestrate the complete Recursive Analysis with Gated Execution cycle.
- `rage-research` — gather and structure evidence.
- `rage-gate` — define and evaluate the execution gate.
- `rage-execute` — perform one bounded admitted action.
- `rage-evaluate` — verify the resulting state against the gate.
- `rage-recurse` — feed evidence into the next loop and detect useless retries.

`AGENTS.md` remains repository-wide authority. Skills refine a task phase; they do not override repository instructions, authorization boundaries, or observed state.