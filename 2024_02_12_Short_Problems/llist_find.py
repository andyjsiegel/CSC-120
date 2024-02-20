class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    # getter for the _value attribute
    def value(self):
        return self._value
    
    # getter for the _next attribute
    def next(self):
        return self._next
        
    def __str__(self):
        return str(self._value) + "; "
    
class LinkedList:
    def __init__(self):
        self._head = None

    # add a node to the head of the list
    def add(self, node):
        node._next = self._head
        self._head = node
        
    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string
    
    def find(self, value):
        curr_node = self._head
        while curr_node != None:
            if value == curr_node.value():
                return True
            curr_node = curr_node.next()
        return False

ll = LinkedList()
ll.add(Node(-8))
ll.add(Node(4))
ll.add(Node(4))
print( ll.find(4))