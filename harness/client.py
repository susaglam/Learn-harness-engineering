"""Build a provider-agnostic, Anthropic-compatible client from environment.

Reads from `.env` (via python-dotenv if installed):
    ANTHROPIC_API_KEY   required for real calls
    MODEL_ID            defaults to claude-sonnet-4-6
    ANTHROPIC_BASE_URL  optional; set it to use an Anthropic-compatible provider

The anthropic SDK is imported lazily inside get_client() so that eval scripts
which use a fake model don't need the SDK installed at all.
"""
from __future__ import annotations

import os

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # dotenv is optional; env vars may be set another way
    pass


def get_model() -> str:
    """The model id to use. Override with MODEL_ID in .env."""
    return os.environ.get("MODEL_ID", "claude-sonnet-4-6")


def get_client():
    """An Anthropic (or Anthropic-compatible) client configured from env."""
    from anthropic import Anthropic  # lazy: only needed for real model calls

    kwargs = {}
    base_url = os.environ.get("ANTHROPIC_BASE_URL")
    if base_url:
        kwargs["base_url"] = base_url
    # ANTHROPIC_API_KEY is picked up from the environment automatically.
    return Anthropic(**kwargs)
