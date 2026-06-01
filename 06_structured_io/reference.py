"""
Lesson 06 - Structured I/O  (reference implementation)

When you need machine-readable output from the model, don't hope it returns
clean JSON -- validate it against a schema and, on mismatch, hand the error
back so the model can correct itself. validate() and parse_and_validate() are
given; you build the retry loop.
"""
from __future__ import annotations

import json


class ValidationError(Exception):
    pass


def validate(obj, schema: dict):
    """schema maps required field name -> expected Python type."""
    if not isinstance(obj, dict):
        raise ValidationError(f"expected an object, got {type(obj).__name__}")
    for field, typ in schema.items():
        if field not in obj:
            raise ValidationError(f"missing field '{field}'")
        if not isinstance(obj[field], typ):
            raise ValidationError(f"field '{field}' must be {typ.__name__}")
    return obj


def parse_and_validate(text: str, schema: dict):
    try:
        obj = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid JSON: {exc}")
    return validate(obj, schema)


def request_structured(model_fn, schema: dict, max_retries: int = 3):
    """Ask model_fn(feedback)->text for output matching `schema`.

    On a validation failure, retry with corrective feedback. Returns
    (obj, attempts) on success; raises ValidationError if still invalid.
    """
    feedback = ""
    last_err = None
    for attempt in range(1, max_retries + 1):
        text = model_fn(feedback)
        try:
            return parse_and_validate(text, schema), attempt
        except ValidationError as exc:
            last_err = exc
            feedback = (
                f"Your previous output was invalid: {exc}. "
                "Return ONLY valid JSON matching the schema."
            )
    raise ValidationError(f"still invalid after {max_retries} attempts: {last_err}")
