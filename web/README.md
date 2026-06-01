# Web Preview

A **zero-build, self-contained** static preview of the course — a single
`index.html` you open directly in a browser (no server, no `npm install`).

Deliberately tiny: unlike the original course's full Next.js site, this just
renders the existing markdown (README, curriculum, docs, and every lesson's
`README.en.md` / `README.tr.md`) with a sidebar, an **EN/TR language toggle**,
and syntax highlighting. The content shape stays in the markdown; the preview is
static and agnostic.

## Use

```sh
python scripts/build_web.py     # regenerates web/index.html from the markdown
```

Then open `web/index.html` in any browser. Re-run after editing markdown.

> `web/index.html` is a generated artifact (git-ignored). The source of truth is
> the markdown across the repo plus `scripts/build_web.py`.
