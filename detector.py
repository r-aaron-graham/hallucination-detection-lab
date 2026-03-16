"""Simple hallucination detection heuristics.

This module implements basic functions that quantify how much of an answer is grounded in the
provided context and whether citations are present.  These heuristics are by no means
comprehensive or foolproof but can serve as a baseline for further research.
"""

from __future__ import annotations

import re
from typing import Iterable, Tuple


def tokenize(text: str) -> Iterable[str]:
    """Tokenize text on whitespace and punctuation.

    For simplicity we lowercase and split on non‑alphanumeric characters.  This is not
    language‑aware but suffices for a basic overlap measure.
    """
    return [t for t in re.split(r"\W+", text.lower()) if t]


def groundedness_score(context: str, answer: str) -> float:
    """Compute the fraction of answer tokens that also appear in the context.

    :param context: Source material that the model should rely on
    :param answer: Generated answer to evaluate
    :return: A float between 0 and 1 indicating overlap (1 = fully grounded)
    """
    ctx_tokens = set(tokenize(context))
    ans_tokens = tokenize(answer)
    if not ans_tokens:
        return 0.0
    overlap = sum(1 for tok in ans_tokens if tok in ctx_tokens)
    return overlap / len(ans_tokens)


def has_citations(answer: str) -> bool:
    """Return True if the answer contains bracketed citation markers like `[1]` or `[a]`."""
    return bool(re.search(r"\[[0-9a-zA-Z]+\]", answer))


def evaluate_answer(context: str, answer: str, threshold: float = 0.2) -> Tuple[bool, float]:
    """Evaluate whether an answer is likely hallucinated.

    An answer is flagged as hallucinated if its groundedness score is below the given threshold
    *or* if it lacks citations.  The threshold can be tuned based on empirical results.

    :param context: The source context
    :param answer: The generated answer
    :param threshold: Minimum groundedness score required to avoid flagging
    :return: Tuple of (is_hallucinated, score)
    """
    score = groundedness_score(context, answer)
    citations_present = has_citations(answer)
    hallucinated = score < threshold or not citations_present
    return hallucinated, score