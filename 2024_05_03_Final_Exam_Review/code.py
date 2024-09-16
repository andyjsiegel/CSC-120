class Stack:
    def __init__(self):
        self._items = []
    def push(self , value):
        self._items.append(value)
    def pop(self):
        return self._items.pop()
    def is_empty(self):
        return self._items == []
    def __str__(self):
        return f"Stack({self ._items})"
    
class Queue:
    def __init__(self):
        self._items = []
    def push(self , value):
        self._items.insert(0, value)
    def pop(self):
        return self._items.pop()
    def is_empty(self):
        return self._items == []
    def __str__(self):
        return f"Queue({self ._items})"
    
class BinaryTree:
    def __init__(self , value):
        self._value = value
        self._left = None
        self._right = None
    def value(self):
        return self._value
    def left(self):
        return self._left
    def right(self):
        return self._right
    def insert_right(self, value):
        if self._right == None:
            self._right = BinaryTree(value)
        else:
            t = BinaryTree(value)
            t._right = self._right
            self._right = t
    def insert_left(self, value):
        if self._left == None:
            self._left = BinaryTree(value)
        else:
            t = BinaryTree(value)
            t._left = self._left
            self._left = t

class LinkedList:
    def __init__(self):
        self._head = None
    def add(self, new):
        new._next = self ._head
        self._head = new
    def __str__(self):
        s = ""
        cur = self ._head
        while cur != None:
            s += f"[{cur._value}]"
            cur = cur._next
        return s
    def process_duplicates(self):
        count_dict = {}
        prev = None
        current = self._head
        while current is not None:
            if current.value() in count_dict:
                count_dict[current.value()] += 1
                prev._next = current.next()
            else:
                count_dict[current.value()] = 1
                prev = current
            current = current.next()
        return count_dict
    
class Node:
    def __init__(self , value):
        self._value = value
        self._next = None
    def value(self):
        return self._value
    def next(self):
        return self._next
    def set_value(self , val):
        self ._value = val
    def set_next(self, node):
        self._next = node

def reverse_list(alist):
    if len(alist) <= 1:
        return alist
    else:
        return [alist[-1]] + reverse_list(alist[:-1])

# print(reverse_list([2, 3, 4]))  # Output: [4, 3, 2]
# print(reverse_list([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]
# print(reverse_list([]))  # Output: []

def evensInTree(tree: BinaryTree):
    if tree is None:
        return []
    else:
        if tree.value() % 2 == 0:
            val = [tree.value()]
        else:
            val = []
        return val + evensInTree(tree.left()) + evensInTree(tree.right())

# tree = BinaryTree(6)
# tree.insert_left(8)
# tree.insert_left(5)
# tree.insert_right(9)
# tree.insert_right(4)
# tree.insert_left(0)
# print(evensInTree(tree))
# [6,0,8,4]

def tree_height(tree: BinaryTree):
    if tree is None:
        return 0
    elif tree.left() is None and tree.right() is None:
        return 0
    else:
        return 1 + max(tree_height(root.left()), tree_height(root.right()))


root = BinaryTree(1)
right_subtree = BinaryTree(3)
right_subtree.insert_right(5)
right_subtree.insert_left(4)
root.insert_right(right_subtree)
root.insert_left(2)
print("Height of the tree:", tree_height(root))  # Output: 2