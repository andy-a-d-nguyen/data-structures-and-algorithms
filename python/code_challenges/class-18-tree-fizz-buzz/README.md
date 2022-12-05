# Challenge Summary

Write a function called fizz buzz tree

- Arguments: k-ary tree
- Return: new k-ary tree

Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

- If the value is divisible by 3, replace the value with "Fizz"
- If the value is divisible by 5, replace the value with "Buzz"
- If the value is divisible by 3 and 5, replace the value with "FizzBuzz"
- If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process

![Tree Fizz Buzz](code_challenge_18.jpg)

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
pytest -v tests/code_challenges/test_tree_fizz_buzz.py
```

To deactivate the virtual environment:

```bash
deactivate
```

## Link to Code

[Link to Code](../code_challenges/../tree_fizz_buzz.py)
