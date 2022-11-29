# Challenge Summary

Write a function called `breadth_first` which takes a tree and returns a list of all values in the tree in the order they were encountered

## Whiteboard Process

![Breadth First Traversal](code_challenge_17.jpg)

## Approach & Efficiency

I whiteboarded the problem domain, test cases and edge cases and outlined a basic pseudocode and solution to the problem domain.

Complexity:

Time: O(N)
Space: O(N)

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
pytest -v tests/code_challenges/test_tree_breadth_first.py
```

To deactivate the virtual environment:

```bash
deactivate
```

## Link to Code

[Link to Code](../code_challenges/../tree_breadth_first.py)
