class LinkedList: 
    def __init__(self): 
        self._head = None 
        # add a node to the head 
    def add(self, new): 
        new._next = self._head 
        self._head = new 
    # remove a node from the head 
    def remove(self): 
        if self._head == None: 
            return None 
        node = self._head 
        self._head = node._next 
        node._next = None 
        return node

class Node: 
    def __init__(self, value):  
        self._value = value  
        self._next = None 
    def value(self): 
        return self._value  

class Stack: 
    def __init__(self): 
        self._items = LinkedList()  
    def push(self, item):
        node = Node(item)
        self._items.add(node)
    def pop(self):
        return self._items.remove().value()
    def is_empty(self):
        return self._items is None
    
class Queue: 
    def __init__(self): 
        self._items = []
    def enqueue(self, item): 
        self._items.append(item)
    def dequeue(self):
        if self._items:  # Check if queue is not empty before dequeueing
            self._items.pop(0)