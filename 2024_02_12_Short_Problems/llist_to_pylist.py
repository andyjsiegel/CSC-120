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
    
    def linkedlist_to_plist(self):
        list_ = []
        curr_node = self._head
        while curr_node != None:
            list_.append(curr_node.value())
            curr_node = curr_node.next()

        return list_
    
def main():
    ll = LinkedList()
    ll.add(Node("hello"))
    return ll.linkedlist_to_plist()

print(main())