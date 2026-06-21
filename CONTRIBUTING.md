# Contributing

Thanks for helping improve **Learn Harness Engineering**. The course is
eval-driven: every lesson is a failing test a learner makes pass, so the bar for
a change is simple — **`python run_all_evals.py` must stay green.**

## The 5-file lesson contract

Each lesson lives in `NN_<slug>/` and ships exactly five files:

| File | Role |
|---|---|
| `README.en.md` | the narrative: the mechanism, *why* it matters, the design choices |
| `README.tr.md` | the Turkish narrative (keep terms in English + an inline gloss on first use) |
| `reference.py` | the complete, correct implementation |
| `stub.py` | the same, with the crucial part replaced by a `TODO` the learner fills |
| `eval.py` | imports the learner's `stub.py` (or `reference.py`) and checks it |

## The RED → GREEN rule

- With the **stub**, the eval must be genuinely **RED**: at least one check FAILS
  (not just a crash — a crash is a broken eval, see below).
- With the **reference** (`LHE_SOLUTION=1`), the eval must be fully **GREEN**.

Run a single lesson both ways:

```sh
python NN_lesson/eval.py                       # RED   (tests stub.py)
# PowerShell:
$env:LHE_SOLUTION=1; python NN_lesson/eval.py  # GREEN (tests reference.py)
```

Run the whole suite (this is exactly what CI runs):

```sh
python run_all_evals.py
```

## Write evals that can't be cheated

An eval's job is to **reject wrong implementations**, not just accept the right
one. Before you submit, ask: *could a trivial or wrong stub pass this?* Make the
mechanism load-bearing — feed inputs where a shortcut gives the wrong answer.
A good eval goes RED for the obvious cheat, not only for an empty stub.

## Keep EN and TR in sync

The two language tracks must stay aligned in shape. If you change a lesson's
mottos, "what you build", or `README` structure, update **both** `README.en.md`
and `README.tr.md`, and the matching row in `CURRICULUM.md` / `CURRICULUM.tr.md`.
New technical terms should be glossed inline in TR and, if recurring, added to
`docs/terminoloji.tr.md` (and `docs/glossary.md`).

## Scaffolding & tooling

- `python scripts/scaffold_lessons.py` — regenerate stub READMEs for any new lesson folders.
- `python scripts/build_web.py` — regenerate the static `web/index.html` preview.
- New lessons should follow the "one mechanism, one motto, one failing test, one fix"
  rule from [docs/methodology.md](./docs/methodology.md).

## PR checklist

- [ ] `python run_all_evals.py` is green (23/23, RED stub → GREEN reference).
- [ ] The eval rejects an obvious wrong/cheating stub, not just an empty one.
- [ ] EN and TR READMEs both updated; mottos match `CURRICULUM.md` / `.tr.md`.
- [ ] New terms glossed inline (TR) and added to the glossaries if recurring.
