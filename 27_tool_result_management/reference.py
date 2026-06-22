"""
Lesson 27 - Tool-Result Management  (reference implementation)

A tool can return megabytes (a full log, a giant file). Feeding that straight
back blows your context budget (Lesson 07). Store the full output as an
ARTIFACT, and feed the model a bounded head+tail excerpt with an omission marker
and a handle to fetch the rest. store_result() is given; you build the summary.
"""
from __future__ import annotations


def store_result(artifacts, key, full_text):
    """Persist the full output; return the handle the model can fetch later."""
    artifacts[key] = str(full_text)
    return key


def summarize_result(text, key, max_chars=200, keep=80):
    """Bound a large result to a head+tail excerpt + omission marker + handle.

    If text fits in max_chars, return it unchanged. Otherwise keep the first and
    last `keep` chars and note how many were omitted and where the full copy is.
    """
    text = str(text)
    if len(text) <= max_chars:
        return text
    omitted = len(text) - 2 * keep
    return (f"{text[:keep]}\n"
            f"...[{omitted} chars omitted; full result at artifact '{key}']...\n"
            f"{text[-keep:]}")
