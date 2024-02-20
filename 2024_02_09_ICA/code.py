class LinkedList:
    def double(self, element):
        return element*2
    def __init__(self):
        self._head = None
    def is_empty(self):
        return self._head == None
    def head(self):
        return self._head
    def add(self, new):
        new._next = self._head
        self._head = new
    
    def print_elements(self):
        current = self._head
        while current != None:
            print(str(self.double(current._value)))
            current = current._next

class Node: 
    def __init__(self, value):  
        self._value = value 
        self._next = None

my_list = LinkedList()
this_node = Node(3)
my_list.add(this_node)
this_node = Node(20)
my_list.add(this_node)

my_list.print_elements()