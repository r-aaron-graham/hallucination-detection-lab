# Hallucination detection lab

A lexical baseline for response evaluation. `detector.py` measures the fraction
of answer tokens appearing in a source context and checks for a bracketed
citation marker. It flags answers below a configurable overlap threshold or
without a marker.

## Run the example

From the repository root:

```bash
python -c "from detector import evaluate_answer; print(evaluate_answer('Solar panels convert sunlight into electricity.', 'Solar panels convert sunlight into electricity [1].', 0.3))"
```

The flag is `False` and the overlap score is about `0.8571` for this fixture.
The marker contributes a token absent from the context. Word variations,
negation, and factual correctness need further evaluation. A citation marker
does not verify that the cited source exists or supports a claim.

## Verify

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

The tests exercise overlap, citation markers, and threshold decisions. The
word-variation example has exactly 0.5 lexical overlap.
