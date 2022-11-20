# Trees

Implement a binary tree class and a binary search tree class

## Challenge

### Node

- Create a Node class that has properties for the value stored in the node, the left child node, and the right child node

### Binary Tree

- Create a Binary Tree class
  - Define a method for each of the depth first traversals:
    - Pre-order
    - In-order
    - Post-order
  - Each depth first traversal method should return an array of values, ordered appropriately

### Binary Search Tree

- Create a Binary Search Tree class
  - This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
    - Add
      - Arguments: value
      - Return: nothing
      - Adds a new node with that value in the correct location in the binary search tree
    - Contains
      - Argument: value
      - Returns: boolean indicating whether or not the value is in the tree at least once

## Approach & Efficiency

My approach was to run each test provided one by one and then writing the minimum amount of code needed to make each test pass and refactoring as necessary.

Big O space/time:

- Binary Tree
  - `pre_order`:
    - Space: O(N)
    - Time: O(N)
  - `in_order`:
    - Space: O(N)
    - Time: O(N)
  - `post_order`:
    - Space: O(N)
    - Time: O(N)
- Binary Search Tree
  - `add`:
    - Space: O(1)
    - Time: O(log N)
  - `contains`:
    - Space: O(1)
    - Time: O(log N)

## API

- Binary Tree:
  - `pre-order`: Add the values in the nodes of the binary tree to a list in the manner root -> left -> right and return the list
  - `in-order`: Add the values in the nodes of the binary tree to a list in the manner left -> root -> right and return the list
  - `post-order`: Add the values in the nodes of the binary tree to a list in the manner left -> right -> root and return the list
- Binary Search Tree:
  - `add`: Add a node to the tree at the appropriate place
  - `contains`: Return whether a value is in the binary search tree

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
pytest -v tests/data_structures/test_binary_search_tree.py tests/data_structures/test_binary_tree.py
```

To deactivate the virtual environment:

```bash
deactivate
```
