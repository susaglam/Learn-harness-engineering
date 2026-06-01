#!/usr/bin/env python3
"""Generate a self-contained static preview of the course at web/index.html.

Reads the repo's markdown (README, CURRICULUM, docs, and each lesson's
README.en.md / README.tr.md), embeds it into a single HTML file, and renders it
client-side with marked + highlight.js (CDN). No build step, no server: open
web/index.html in a browser. Re-run after editing markdown.

    python scripts/build_web.py
"""
from __future__ import annotations

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "web")
OUT = os.path.join(OUT_DIR, "index.html")


def read(rel: str) -> str:
    path = os.path.join(ROOT, rel)
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            return f.read()
    return ""


def lesson_title(folder: str) -> str:
    num, _, rest = folder.partition("_")
    return f"{num} · " + rest.replace("_", " ").title()


def build_pages():
    pages = []

    def add(pid, title, group, en_rel, tr_rel):
        en, tr = read(en_rel), read(tr_rel)
        if en or tr:
            pages.append({"id": pid, "title": title, "group": group, "en": en, "tr": tr})

    add("home", "Home", "Intro", "README.md", "README.tr.md")
    add("curriculum", "Curriculum", "Intro", "CURRICULUM.md", "CURRICULUM.tr.md")
    add("philosophy", "Philosophy", "Intro", "docs/philosophy.md", "docs/philosophy.tr.md")
    add("methodology", "Methodology", "Intro", "docs/methodology.md", "docs/methodology.tr.md")
    add("glossary", "Glossary", "Intro", "docs/glossary.md", "docs/terminoloji.tr.md")

    for name in sorted(os.listdir(ROOT)):
        if len(name) >= 3 and name[:2].isdigit() and name[2] == "_" \
                and os.path.isdir(os.path.join(ROOT, name)):
            add(name, lesson_title(name), "Lessons",
                f"{name}/README.en.md", f"{name}/README.tr.md")
    return pages


HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Learn Harness Engineering</title>
<!-- CDN libs are version-pinned. For a PUBLIC deployment also add Subresource
     Integrity: integrity="sha384-..." on each tag (omitted here because a wrong
     hash would block the script entirely; fine for a local trusted preview). -->
<link rel="stylesheet" crossorigin="anonymous" href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/styles/github-dark.min.css">
<style>
  :root { --bg:#0d1117; --panel:#161b22; --border:#30363d; --fg:#e6edf3; --muted:#8b949e; --accent:#58a6ff; }
  * { box-sizing: border-box; }
  body { margin:0; background:var(--bg); color:var(--fg); font:16px/1.65 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif; }
  .app { display:flex; min-height:100vh; }
  aside { width:300px; flex:0 0 300px; background:var(--panel); border-right:1px solid var(--border); padding:18px 14px; overflow-y:auto; height:100vh; position:sticky; top:0; }
  aside h1 { font-size:15px; margin:0 0 4px; }
  aside .tag { color:var(--muted); font-size:12px; margin-bottom:14px; }
  .grp { color:var(--muted); text-transform:uppercase; font-size:11px; letter-spacing:.08em; margin:16px 0 6px; }
  nav a { display:block; padding:5px 8px; border-radius:6px; color:var(--fg); text-decoration:none; font-size:14px; cursor:pointer; }
  nav a:hover { background:#21262d; }
  nav a.active { background:#1f6feb33; color:var(--accent); }
  main { flex:1; min-width:0; }
  .topbar { display:flex; justify-content:flex-end; gap:6px; padding:12px 28px; border-bottom:1px solid var(--border); position:sticky; top:0; background:var(--bg); z-index:2; }
  .toggle button { background:var(--panel); color:var(--fg); border:1px solid var(--border); padding:5px 12px; border-radius:6px; cursor:pointer; font-size:13px; }
  .toggle button.active { background:var(--accent); color:#0d1117; border-color:var(--accent); }
  .content { max-width:860px; margin:0 auto; padding:8px 28px 80px; }
  .content h1{border-bottom:1px solid var(--border);padding-bottom:.3em} .content h2{border-bottom:1px solid var(--border);padding-bottom:.25em;margin-top:1.6em}
  .content a { color:var(--accent); }
  .content code { background:#161b22; padding:.15em .4em; border-radius:5px; font-size:.9em; }
  .content pre { background:#161b22; border:1px solid var(--border); border-radius:8px; padding:14px; overflow:auto; }
  .content pre code { background:none; padding:0; }
  .content table { border-collapse:collapse; } .content th,.content td{ border:1px solid var(--border); padding:6px 12px; }
  .content blockquote { border-left:3px solid var(--accent); margin:0; padding:.2em 1em; color:var(--muted); }
</style>
</head>
<body>
<div class="app">
  <aside>
    <h1>Learn Harness Engineering</h1>
    <div class="tag">Build the environment that turns a model into a real agent &mdash; and measure it.</div>
    <nav id="nav"></nav>
  </aside>
  <main>
    <div class="topbar"><div class="toggle">
      <button id="enBtn" class="active" onclick="setLang('en')">English</button>
      <button id="trBtn" onclick="setLang('tr')">T&uuml;rk&ccedil;e</button>
    </div></div>
    <div class="content" id="content"></div>
  </main>
</div>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.0/marked.min.js" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/dompurify@3.0.11/dist/purify.min.js" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js" crossorigin="anonymous"></script>
<script>/*DATA*/</script>
<script>
  let lang = "en", current = DATA[0] ? DATA[0].id : null;
  function byId(id){ return DATA.find(p => p.id === id); }
  function buildNav(){
    const nav = document.getElementById("nav"); let html = ""; let group = null;
    for (const p of DATA){
      if (p.group !== group){ group = p.group; html += '<div class="grp">'+group+'</div>'; }
      html += '<a data-id="'+p.id+'" onclick="go(\''+p.id+'\')">'+p.title+'</a>';
    }
    nav.innerHTML = html;
  }
  function render(){
    const p = byId(current); if(!p) return;
    let md = p[lang] || p.en || p.tr || "*(no content)*";
    // Sanitize the rendered markdown before injecting (defense-in-depth; the
    // course's own Lesson 13 is about not trusting rendered/external content).
    document.getElementById("content").innerHTML = DOMPurify.sanitize(marked.parse(md));
    document.querySelectorAll("#content pre code").forEach(b => { try{ hljs.highlightElement(b); }catch(e){} });
    document.querySelectorAll("#nav a").forEach(a => a.classList.toggle("active", a.dataset.id === current));
    document.getElementById("enBtn").classList.toggle("active", lang==="en");
    document.getElementById("trBtn").classList.toggle("active", lang==="tr");
    window.scrollTo(0,0);
  }
  function go(id){ current = id; location.hash = id; render(); }
  function setLang(l){ lang = l; render(); }
  buildNav();
  if (location.hash && byId(location.hash.slice(1))) current = location.hash.slice(1);
  render();
</script>
</body>
</html>
"""


def main():
    pages = build_pages()
    # Escape every '<' as the JSON unicode escape <. JSON.parse restores it
    # and marked renders identically, but no '</script>', '<script', or '<!--'
    # can ever survive in the embedded <script> block (robust HTML-in-JS embed).
    data_js = "const DATA = " + json.dumps(pages, ensure_ascii=False).replace("<", "\\u003c") + ";"
    html = HTML.replace("/*DATA*/", data_js)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    kb = round(len(html.encode("utf-8")) / 1024)
    print(f"Wrote {OUT}  ({len(pages)} pages, {kb} KB)")
    print("Open it in a browser. Re-run this script after editing any markdown.")


if __name__ == "__main__":
    main()
