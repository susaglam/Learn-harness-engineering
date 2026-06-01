"""Shared, provider-agnostic harness infrastructure.

Lessons 2+ import from here so they don't re-teach the basics:
    from harness.loop import run_agent
    from harness.client import get_client, get_model
    from harness.evals import check, report

Lesson 01 deliberately re-implements the loop itself — that's the point of it.
"""
