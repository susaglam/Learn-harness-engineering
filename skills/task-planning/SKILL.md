# Task Planning Skill
Break a multi-step goal into an ordered, status-tracked todo list before acting.

## When to use
Use whenever a request needs more than ~2 steps, touches multiple files/systems,
or is easy to drift on. Skip it for trivial one-shot answers.

## Procedure
1. Restate the goal in a single sentence.
2. Decompose it into 3-7 concrete, individually verifiable steps.
3. Emit them with the TodoWrite tool, each `{content, status}`.
4. Keep exactly one step `in_progress`; finish it; re-render; repeat.
5. Stop when every step is `completed`.

## Example
```python
# illustrative pseudocode for the TodoWrite tool (Lesson 05 surfaces TodoStore.write)
todo_write([
    {"content": "Reproduce the bug with a failing test", "status": "in_progress"},
    {"content": "Fix the root cause",                     "status": "pending"},
    {"content": "Re-run the suite and confirm green",     "status": "pending"},
])
```

## Ties to
Lesson 05 (Planning). The rendered list is working memory for the *task*.
