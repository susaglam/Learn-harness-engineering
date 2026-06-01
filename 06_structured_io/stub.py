"""
Lesson 06 - Structured I/O  (YOUR implementation)

validate() and parse_and_validate() are given. Implement request_structured:
the validate-then-retry-with-feedback loop.

Run:  python 06_structured_io/eval.py     # RED until the TODO is done
"""
from __future__ import annotations

import json


class ValidationError(Exception):
    pass


def validate(obj, schema: dict):
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
    # =========================================================================
    # TODO(you): loop up to max_retries times.
    #   - feedback starts as ""  (empty for the first attempt)
    #   - text = model_fn(feedback)
    #   - try: return (parse_and_validate(text, schema), attempt_number)
    #   - except ValidationError as exc: set feedback to a corrective message
    #     that includes str(exc), then loop again.
    #   - If all attempts fail, raise ValidationError(...).
    # =========================================================================
    raise NotImplementedError("Implement request_structured - see the TODO above")
