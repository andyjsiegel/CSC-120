class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0

def reverse(s):
    stack = Stack()
    reversed_string = ""
    for char in s:
        stack.push(char)
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string

print(reverse("Palindrome"))

def balanced(s):
    stack = Stack()
    for char in s:
        if char == '[':
            stack.push(char)
        if char == ']':
            stack.pop()
    return stack.is_empty()

print(balanced('[[[[]]]'))
    