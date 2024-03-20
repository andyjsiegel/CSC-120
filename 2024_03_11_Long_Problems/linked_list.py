"""
File: linked_list.py
Author: Andy Siegel
Course: CSC 120, Spring 2024
Purpose: This program creates the Node
    and LinkedList classes to be used in
    friends.py
"""
class LinkedList:
    
    def __init__(self):
        """
        This function initializes the LinkedList
        by setting its head to None.
        """
        self._head = None

    def make_friends(self, name1, name2):
        """
        This function adds the node of name1 to
        the node of name2's friends list. If name1's
        node does not exist, it makes one.
        Parameters:
            name1: the name of the first person
            name2: the name of the second person
        Returns:
            None
        """
        exists, node = self.exists(name1)
        if exists:
            node._friends.add(Node(name2))
        else:
            name1_node = Node(name1)
            name1_node._friends.add(Node(name2))
            self.add(name1_node)
        
    def exists(self, name):
        """
        This function takes in a name and looks for
        a node with that name. If it finds one, it
        returns True with the node, otherwise it 
        returns False with None.
        Parameters:
            name: the name of the node to look for.
        Returns:
            A tuple with a True and the node or 
            False and None if the node doesn't 
            exist.
        """
        current = self._head
        while current != None:
            if current.name() == name:
                return True, current
            current = current.next()
        return False, None
    
    # sort the nodes in the list
    # source: long problem for sorting a linked lists
    def sort(self):
        sorted_list = LinkedList()
        while self._head:
            current = self.remove_hd()
            if sorted_list._head is None or \
            current.name() < sorted_list._head.name():
                sorted_list.add(current)
            else:
                prev = sorted_list._head
                while prev.next() and prev.next().name() <= current.name():
                    prev = prev.next()
                self.insert_after(prev, current)

        self._head = sorted_list._head

    # add a node to the head of the list
    # source: long problem for sorting a linked lists
    def add(self, node):
        node._next = self._head
        self._head = node
        
    # remove a node from the head of the list and return the node
    # source: long problem for sorting a linked lists
    def remove_hd(self):
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node

    # insert node2 after node1
    # source: long problem for sorting a linked lists
    def insert_after(self, node1, node2):
        assert node1 != None
        node2._next = node1._next
        node1._next = node2

    # insert node2 after node1
    # source: long problem for sorting a linked lists
    def is_empty(self):
        return self._head == None

    def __str__(self):
        string = ""
        current = self._head
        while current != None:
            current2 = current._friends._head
            string += current.name() + '\n'
            while current2 != None:
                string += "   " + current2.name() + '\n'
                current2 = current2.next()
            current = current.next()
        return string
    
    def intersection(self, other):
        """
        This function takes in a LinkedList to
        compare to the one represented by self
        and returns a new LinkedList with their 
        shared items. 
        Parameters:
            other: the other LinkedList
        Returns:
            intersect_list
        """
        intersect_list = LinkedList()
        current1 = self._head
        while current1:
            current2 = other._head
            while current2:
                if current1.name() == current2.name():
                    intersect_list.add(Node(current1.name()))
                    break
                current2 = current2.next()
            current1 = current1.next()
        return intersect_list


class Node:
    def __init__(self, name):
        """
        This function initializes the Node
        by setting the name to the name of
        the node and setting the _friends 
        attribute to a new LinkedList.
        Parameters:
            name: the name of the person 
            represented by the node.
        """
        self._name = name
        self._friends = LinkedList()
        self._next = None
    
    def name(self):
        return self._name
    
    def get_friends(self):
        return self._friends
    
    def next(self):
        return self._next
    
    def set_next(self, target):
        self._next = target

    def __str__(self):
        string = self._name + ' -> ['
        current = self._friends._head
        while current != None:
            string += current.name() + ', '
            current = current.next()

        return string
