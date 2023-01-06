# Title: Sorting Comparisons

## Challenge Summary

Write functions which sort domain objects. Your functions will receive an array of Movie objects. Each Movie object has a title (string), a year (number), and a list of genres (array of strings). One function will sort the movies by most recent year first. One function will sort the movies, alphabetical by title, but will ignore any leading "A"s, "An"s, or "The"s.

Write tests for your comparator functions. This may necessitate refactoring the code you wrote in part one. Your tests will need to call the comparator functions directly, and make assertions about the response values given test inputs.

## Solution

To run the tests for this code challenge, make sure you cd into the `sorting` directory first.

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
pytest -v tests/test_sorting_comparisons.py
```

To deactivate the virtual environment:

```bash
deactivate
```

## Link to Code

[Link to Code](sorting.py)
