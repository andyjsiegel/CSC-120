class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return self._items == []
    
    def __str__(self):
        return str(self._items)

def decimal2binary(n):
    binary_rep = Stack()
    while n / 2 > 0:
        # print(n % 2)
        binary_rep.push(str(n % 2))
        n = n // 2

    return ''.join(binary_rep._items[::-1])

assert decimal2binary(35) == '100011'
assert decimal2binary(255) == '11111111'
assert decimal2binary(19) == '10011'
assert decimal2binary(233) == '11101001'
print('all tests passed')