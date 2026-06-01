# Subagent Delegation Skill
Delegate noisy or context-heavy sub-tasks to a fresh subagent and keep only its result.

## When to use
When a sub-task would flood the main context -- a large search, reading ten
files, trying three approaches -- or needs an isolated scratch space whose
intermediate steps the parent never needs to see.

## Procedure
1. Phrase the sub-task as a single, self-contained instruction.
2. Run it in a FRESH context: `run_subagent(task, ...)` with no parent history.
3. Return only the final text to the parent; discard the intermediate steps.
4. If several sub-tasks are independent, fan them out in parallel.

## Why it works
Isolation keeps the subagent focused and the parent clean; compression turns a
30-step investigation into one paragraph the parent can act on.

## Ties to
Lesson 08 (Subagents), Lesson 19 (Agent Teams).
