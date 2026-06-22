"""
Lesson 27 - Tool-Result Management  (YOUR implementation)

store_result() is given. Implement summarize_result(): bound a large tool result
to a head+tail excerpt with an omission marker and the artifact handle.

Run:  python 27_tool_result_management/eval.py     # RED until the TODO is done
"""
from __future__ import annotations


def store_result(artifacts, key, full_text):
    artifacts[key] = str(full_text)
    return key


def summarize_result(text, key, max_chars=200, keep=80):
    # =========================================================================
    # TODO(you):
    #   text = str(text)
    #   - if len(text) <= max_chars: return text unchanged.
    #   - else: omitted = len(text) - 2*keep; return a string with:
    #       text[:keep] + a marker noting `omitted` chars + the artifact `key`
    #       + text[-keep:]   (so BOTH the head and the tail survive, plus a handle)
    # =========================================================================
    raise NotImplementedError("Implement summarize_result - see the TODO above")
