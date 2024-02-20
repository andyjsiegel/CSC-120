class LinkedList:
    def __init__(self):
        self._head = None

    def add(self,new):
        new._next = self._head
        self._head = new
        
    def print_elements(self):
        current = self._head
        while current != None:
            print(str(current._value))
            current = current._next

    # define this
    def incr(self):
        current = self._head
        while current != None:
            current._value += 1
            current = current._next

    # define this
    def replace(self, val1, val2):
        current = self._head
        while current != None:
            if current._value == val1:
                current._value = val2
            current = current._next

    # define this
    def add_to_end(self, new):
        if self._head == None: # the list is empty
            self._head = new # add the new node
        else:
            current = self._head
            while current._next != None:
                current = current._next
            current._next = new

    # define this
    def remove_first(self):
        if self._head == None: # check for empty list
            return None
        else:
            n = self._head
            self._head = n._next
            n._next = None
            return n

    def __str__(self):
        string = 'LList -> '
        current = self._head
        while current != None:
            string += str(current)
            current = current._next
        return string

    def get_element(self, n):
        elt = self._head
        while elt != None and n > 0:
            elt = elt._next
            n -= 1
        return elt
    
    def sum_even_positions(self):
        element = self._head
        sum = 0
        n = 0
        while element != None and n % 2 == 0:
            sum += element._value
            element = element._next
            n += 1
    
        return sum
    
class Node:
    def __init__(self,value):
        self._value = value
        self._next = None

    def __str__(self):
        if self._next == None:
            return "None"
        
        return str(self._value)
    
def main(): 
    my_ll = LinkedList()
    n1 = Node(10)
    my_ll.add(n1)
    n2 = Node(20)
    my_ll.add(n2)
    n3 = Node(30)
    my_ll.add(n3)
    n3 = Node(40)
    my_ll.add(n3)

    print(my_ll.sum_even_positions())

main()