class LinkedList:
    def __init__(self):
        self._head = None
    
    # sort the nodes in the list
    def sort(self):
        to_be_sorted = self._head
        sorted = None

        while to_be_sorted is not None:
            curr_element = self.remove()
            if sorted is None or sorted.value() < curr_element.value():
                self.add(curr_element)
            else:
                prev = None
                current = sorted
                while current is not None and current.value() >= curr_element.value():
                    prev = current
                    current = current.next()
                if current is None:
                    self.insert(prev, curr_element)
                else:
                    self.insert(prev, curr_element)

        self._head = sorted
    
    # add a node to the head of the list
    def add(self, node):
        node._next = self._head
        self._head = node
        
    # remove a node from the head of the list and return the node
    def remove(self):
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node
    
    # insert node2 after node1
    def insert(self, node1, node2):
        assert node1 != None
        node2._next = node1._next
        node1._next = node2
    
    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    def __str__(self):
        return str(self._value) + "; "
    
    def value(self):
        return self._value
    
    def next(self):
        return self._next
    
def create_linked_list(filename):
    file = open(filename, 'r')
    for line in file:
        print(line.split())
    

def main():

    # print("hello :3 u just ran main()")
    print('List[ 1; 1; 1; ]')
    # file_name = input()
    # create_linked_list(file_name)