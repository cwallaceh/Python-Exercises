# Valid Parentheses

# Given a string containing just the characters '(', ')' determine if the input string is valid.
# The brackets must close in the correct order "()"


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def valid_parentheses(txt):
    """Using a Stack
    Time Complexity: O(n)
    Auxiliary Space: O(n) for stack."""
    stack = Stack()
    for char in txt:
        if char == '(':
            stack.push(char)
        elif char == ')':
            try:
                stack.pop()
            except IndexError:
                return False
    if stack.items:
        return False
    else:
        return True


print(valid_parentheses('(((((((())))))))'))
print(valid_parentheses(')('))
print(valid_parentheses('((())'))
print(valid_parentheses('(())))'))
