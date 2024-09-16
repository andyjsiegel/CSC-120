class LinkedList:
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
            print(current)
            current = current._next

class Node: 
    def __init__(self, value):  
        self._value = value 
        self._next = None
    def __str__(self):
        return str(self._value)

llistA = LinkedList()

this_node = Node(3)
llistA.add(this_node)

this_node = Node(20)
llistA.add(this_node)

this_node = Node(42)
llistA.add(this_node)

this_node = Node(9)
llistA.add(this_node)

llistB = LinkedList()
llistB.add(Node(69))
llistB.add(Node(420))
llistB.add(Node(1337))
llistB.add(Node(2))


# llistA.print_elements()
# llistB.print_elements()

def compare(llist1: LinkedList, llist2: LinkedList) -> int:
    curA, curB = llist1._head, llist2._head
    while True:
        if curA is not None and curB is None:
            return 1
        elif curA is None and curB is not None:
            return -1
        elif curA is None and curB is None:
            return 0
        
        curA = curA._next
        curB = curB._next

print(compare(llistA, llistB))