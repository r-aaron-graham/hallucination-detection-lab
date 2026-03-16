# Hallucination Detection Lab

This repository provides simple heuristics and utilities for detecting hallucinations in
language model outputs.  Hallucinations occur when a model generates information that is not
supported by the provided context or training data.  Detecting hallucinations is an active
area of research; this project demonstrates lightweight techniques that can serve as
building blocks for more sophisticated evaluators.

## Included components

* `detector.py` – contains functions for measuring the degree to which an answer is grounded
  in a given context and for checking whether citations are present.
* `tests/` – unit tests illustrating how the detection functions work on sample inputs.

## Getting started

Install dependencies and run the tests:

```bash
pip install -r requirements.txt
pytest tests
```

## Approach

The current implementation uses very simple heuristics:

* **Groundedness score**: compute the overlap between the answer tokens and the context tokens.
  A low overlap suggests the answer may include unsupported statements.
* **Citation check**: verify that the answer includes bracketed citation markers (e.g. `[1]`).

These rules are intentionally naive but provide a starting point for building more advanced
hallucination detectors.  In a production environment you could integrate fact extraction,
knowledge graphs, or retrieval‑augmented verification to improve accuracy.