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
        

class Node:
    def __init__(self,value):
        self._value = value
        self._next = None

    def __str__(self):
        if self._next == None:
            nxt = "None"
        else:
            nxt = "->"
        return " |" + str(self._value) + "|:" + nxt


def main():
    # 1. Do all of the following in main():
    #  a) make a linked list called my_ll and add three elements that are ints
    my_ll = LinkedList()
    n1 = Node(10)
    my_ll.add(n1)
    n2 = Node(20)
    my_ll.add(n2)
    n3 = Node(30)
    my_ll.add(n3)

    #  b) use the method print_elements() to print out linked list
    #     use my_ll.print_elements()

    my_ll.print_elements()

    #  c) now use print() to print your linked list
    #     remember that print() implicitly calls str() if it's defined
    #     use print(my_ll)

    print(my_ll)
 
    #  d) take a pic of the output generated for this problem so far to use as the solution

    """
    30
    20
    10
    LList ->  |30|:-> |20|:-> |10|:None
    more tests for remove_first()
    """

    # 2. define incr(), call it, then print the list, take a pic

    my_ll.incr()
    print(my_ll)

    """ LList ->  |31|:-> |21|:-> |11|:None """

    # 3. define replace(),  call it, then print the list, take a pic

    my_ll.replace(31, 69)
    print(my_ll)

    # 4. define add_to_end()  see slides 118 or 119
    # make a node n and add it to the end of the linked list
    # print the linked list and take a pic
    my_ll.add_to_end(Node(420))
    print(my_ll)

    # 5. Challenge: define remove_first(), call on your list, print the list

    first_value = my_ll.remove_first()
    print(first_value)
    print(my_ll)
   
    empty_ll = LinkedList()
    print(empty_ll.remove_first())

    one_element_ll = LinkedList()
    one_element_ll.add(Node(73))
    print(one_element_ll.remove_first())
    # make sure to cover all test cases:
    #    an empty list
    #    a list of one element
    #    a list of many elements
    
main()