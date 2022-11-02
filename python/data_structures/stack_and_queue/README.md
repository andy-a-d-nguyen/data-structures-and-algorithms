# Stacks and Queues

According to <https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-10/resources/stacks_and_queues.html>, a stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

According to <https://www.geeksforgeeks.org/queue-data-structure/>, a queue is defined as a linear data structure that is open at both ends and the operations are performed in First In First Out (FIFO) order.

## Challenge

Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue.

## Approach & Efficiency

My approach was to run each test provided one by one and then writing the minimum amount of code needed to make each test pass and refactoring as necessary.

Big O space/time:

- Stack:
  - `push`:
    - Space: O(1)
    - Time: O(1)
  - `pop`:
    - Space: O(1)
    - Time: O(1)
  - `peek`:
    - Space: O(1)
    - Time: O(1)
  - `is_empty`:
    - Space: O(1)
    - Time: O(1)
- Queue:
  - `enqueue`:
    - Space: O(1)
    - Time: O(N)
  - `dequeue`:
    - Space: O(1)
    - Time: O(1)
  - `peek`:
    - Space: O(1)
    - Time: O(1)
  - `is_empty`:
    - Space: O(1)
    - Time: O(1)

## API

Stack:

- `push`: Adds a new node with that value to the top of the stack
- `pop`: Removes the node from the top of the stack and returns its value. Raises exception when called on an empty stack
- `peek`: Returns the value of the node located at the top of the stack. Raises exception when called on an empty stack
- `is_empty`: Returns boolean indicating whether the stack is empty

Queue:

- `enqueue`: Adds a new node with that value to the back of the queue with an O(1) Time performance
- `dequeue`: Removes the node from the front of the queue and returns the value from node from the front of the queue. Throws exception when called on an empty queue
- `peek`: Returns the value of the node located at the front of the queue. Raises exception when called on an empty
  queue
- `is_empty`: Returns boolean indicating whether the queue is empty

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
pytest -v tests/data_structures/test_stack.py tests/data_structures/test_queue.py
```

To deactivate the virtual environment:

```bash
deactivate
```
