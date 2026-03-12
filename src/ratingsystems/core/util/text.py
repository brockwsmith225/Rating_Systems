import math
from typing import Any


def center(text: Any, columns: int) -> str:
    text = str(text)
    if len(text) > columns:
        return f"{text[:columns-3]}..."
    return (" " * math.floor((columns - len(text)) / 2)) + text + (" " * math.ceil((columns - len(text)) / 2))


def ljustify(text: Any, columns: int) -> str:
    text = str(text)
    if len(text) > columns:
        return f"{text[:columns-3]}..."
    return text + (" " * (columns - len(text)))


def rjustify(text: Any, columns: int) -> str:
    text = str(text)
    if len(text) > columns:
        return f"{text[:columns-3]}..."
    return (" " * (columns - len(text))) + text
