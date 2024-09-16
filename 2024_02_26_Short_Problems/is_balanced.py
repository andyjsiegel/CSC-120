class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return self._items == []
    
    def __len__(self):
        return len(self._items)
    def __str__(self):
        return str(self._items)



def is_balanced(text, lsym, rsym):
    delimiters_stack = Stack()
    for char in text:
        if char == lsym:
            delimiters_stack.push(char)
        if char == rsym:
            if delimiters_stack.is_empty() or delimiters_stack.pop() != '[':
                return False
            return delimiters_stack.is_empty()



assert is_balanced('{}[][]()') == True, "Test passed for input '{}'{}', expected output=True"
assert is_balanced('({)}') == False, "Test failed for input '{}'{}', expected output=False, actual output=True"
assert is_balanced('[[{{(())}}]]') == True, "Test passed for input '{}'{}', expected output=True"
assert is_balanced('((()}))') == False, "Test failed for input '{}'{}', expected output=False, actual output=True"

print(is_balanced('{}[][]()'))  # Expected output: True
print(is_balanced('({)}'))  # Expected output: False
print(is_balanced('[[{{(())}}]]'))  # Expected output: True
print(is_balanced('((()}))'))  # Expected output: False
