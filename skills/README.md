# Example Skills

[English](./README.md) | [Türkçe](./README.tr.md)

A **skill** is a package of on-demand knowledge: a `SKILL.md` whose first non-heading
line is a one-line description (the cheap *manifest* entry) and whose body is the full
procedure (loaded only when needed). This is the format **Lesson 10 (Skill
Loading)** teaches your `SkillManager` to read.

These three example skills map onto the curriculum:

| Skill | What it teaches | Ties to |
|---|---|---|
| `task-planning/` | plan before acting (TodoWrite) | Lesson 05 |
| `subagent-delegation/` | offload noisy work, keep the result | Lesson 08, 19 |
| `mcp-connection/` | borrow an MCP server's tools | Lesson 11 |

## See it work

```sh
python skills/demo.py
```

`demo.py` loads the **Lesson 10 reference `SkillManager`** and runs it against
*this* directory — printing the cheap `manifest()` (names + descriptions) and a
full `load()` of one skill. That's the progressive-disclosure principle on real
content: the index is always present; the body arrives on demand.

## Extend it

Add your own skill: create `skills/<name>/SKILL.md` with a `# Title`, a one-line
description on the next line, and a procedural body. It will appear in
`manifest()` automatically — no code changes. As you reach Lessons 16+ you'll
naturally grow this directory.
