"""
File: linkedlist_sort.py
Author: Andy Siegel
Course: CSC 120, Spring 2024
Purpose: This python code creates two classes
    a LinkedList class, and a Node class, then
    takes in a file name and from the file makes
    a LinkedList with the numbers of each line in
    the file. The LinkedList is then sorted in
    descending order and printed out. 
"""

class LinkedList:
    def __init__(self):
        self._head = None
    
    # sort the nodes in the list
    def sort(self):
        """
        This method sorts the linked list in descending order
        then reassigns self._head to the new linked list's head 
        Args: 
            none
        Returns: 
            none
        """
        sorted_list = LinkedList()
        while self._head:
            current = self.remove()
            if sorted_list._head is None or \
            current._value >= sorted_list._head._value:
                sorted_list.add(current)
            else:
                prev = sorted_list._head
                while prev._next and prev._next._value > current._value:
                    prev = prev._next
                self.insert(prev, current)

        self._head = sorted_list._head

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

    def is_empty(self):
        return self._head == None
    
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
    """
    This function creates a linked list using data 
    from a given file, then sorts the list in
    descending order, then prints it out.  
    Args:
        filename: the name of the file containing the data 
        for the linked list
    Returns:
        None
    """
    file = open(filename, 'r')
    linked_list = LinkedList()
    for line in file:
        nums_list = line.split()
        for num in nums_list:
            linked_list.add(Node(int(num)))
    file.close()
    
    linked_list.sort()
    print(linked_list)
            
    

def main():
    file_name = input()
    create_linked_list(file_name)

main()