# Challenge Summary

Implement a Queue using 2 Stacks

## Whiteboard Process

![Stack Queue Pseudo](stack_queue_pseudo.jpg)

## Approach & Efficiency

I whiteboarded the problem domain, test cases and edge cases and outlined a basic pseudocode and solution to the problem domain.

Complexity:

- `enqueue`:
  - Time: O(1)
  - Space: O(1)
- `dequeue`:
  - Time: O(N)
  - Space: O(1)

## Solution

To run the tests for this code challenge, make sure you `cd` into the `python` directory first.

Then create a virtual environment:

```bash
python3 -m venv .venv
```

Then activate the virtual environment:

```bash
source .venv/bin/activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

To run the tests for this code challenge:

```bash
pytest -v tests/code_challenges/test_stack_queue_pseudo.py
```

To deactivate the virtual environment:

```bash
deactivate
```

## Link to Code

[Link to Code](../../code_challenges/stack_queue_pseudo.py)
