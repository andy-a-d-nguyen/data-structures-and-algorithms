# Challenge Summary

Write a function `kth_from_end` which takes a linked list and a number `k` as an argument and returns the node's value that is `k` places from the tail of the linked list.

## Whiteboard Process

The whiteboard process was done with Daniel Brott and Natalija Germek.

![Linked List Kth From End](linked_list_kth.jpg)


## Approach & Efficiency

Our approach to the solution during the whiteboard process was that we would first find out the length of the linked
list by traversing through it. Then, if k is greater than or equal to the length or smaller than 0, we know k is an
invalid number, and we throw an exception. Then, we create a pointer to the head and iterate from 1 to the length of
the linked list subtracted by k moving to pointer to its next node in the process. Finally, we return the pointer's
value.

Time complexity: O(N)

Space complexity: O(1)

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
pytest -v tests/code_challenges/test_linked_list_kth.py
```

To deactivate the virtual environment:

```bash
deactivate
```

### Link to Code

[Link to Code](../../data_structures/linked_list/linked_list.py)
