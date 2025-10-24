
from __future__ import annotations
from typing import Mapping

def render(template: str, variables: Mapping[str, str]) -> str:
    # Simple {TOKEN} replacement; unknown tokens left as-is
    out = template
    for k, v in variables.items():
        out = out.replace('{' + k + '}', str(v))
    return out
