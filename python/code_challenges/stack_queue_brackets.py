from data_structures.stack_and_queue.stack import Stack


def multi_bracket_validation(string):
    stack = Stack()
    bracket_pairs = {
        "]": "[",
        "}": "{",
        ")": "("
    }
    for char in string:
        if char == "[" or char == "{" or char == "(":
            stack.push(char)
        elif char in bracket_pairs:
            if stack.is_empty() is True:
                return False
            else:
                if stack.peek() == bracket_pairs[char]:
                    stack.pop()
    return stack.is_empty()


def multi_bracket_validation_unoptimized(string):
    stack = Stack()
    for char in string:
        if char == "[" or char == "{" or char == "(":
            stack.push(char)
        elif char == "]":
            if stack.is_empty() is True:
                return False
            else:
                if stack.peek() == "[":
                    stack.pop()
        elif char == "}":
            if stack.is_empty() is True:
                return False
            else:
                if stack.peek() == "{":
                    stack.pop()
        elif char == ")":
            if stack.is_empty() is True:
                return False
            else:
                if stack.peek() == "(":
                    stack.pop()
    return stack.is_empty()
