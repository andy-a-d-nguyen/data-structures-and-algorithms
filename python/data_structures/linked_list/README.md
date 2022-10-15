# Singly Linked List

According to <https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-05/resources/singly_linked_list.html>, a linked list is a data structure that contains nodes that point to the next node in the list. A singly linked list is a linked list that has a reference called a head, and this head represents the first node in the list and each node in the list points to another node or `None`.

## Challenge

Implement a singly linked list

## Approach & Efficiency

After understanding the problem, I started by running each test in `tests/data_structures/test_linked_list.py` one test at a time and then write the necessary code to make the that test pass.

- `insert`: O(1) time, O(1) space
- `includes`: O(N) time, O(1) space
- `__str__`: O(N) time, O(N) space

## API

- `insert`:
  - Arguments: a value
  - Returns: nothing
  - Description: Adds a new node with the input value to the head of the list
- `includes`:
  - Arguments: a value
  - Returns: a boolean
  - Description: Returns true if input value exists in a linked list and false otherwise
- `__str__`:
  - Arguments: none
  - Returns: a string
  - Description: Returns a string representation of all the nodes in a linked list formatted as `"{ a } -> { b } -> { c } -> NULL"`

## Setup

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
pytest -v tests/data_structures/test_linked_list.py
```

To deactivate the virtual environment:

```bash
deactivate
```
