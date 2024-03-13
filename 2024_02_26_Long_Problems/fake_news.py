"""
File: fake_news.py
Author: Andy Siegel
Course: CSC 120, Spring 2024
Purpose: This program takes in a CSV of 
    news articles and their metadata, 
    then uses the csv module to get
    all of their titles, remove
    punctuation, and create a
    LinkedList to count all of the 
    words with a length > 3, then
    print them out. 
"""
import csv, string

class LinkedList:
    """
    This class creates a LinkedList of Nodes 
    which have a word attribute as well as a
    count attribute. There are several 
    helper functions to get various things in
    the LL like the count of the nth node or 
    print every node with a count higher than n
    """
    def __init__(self):
        """
        This functions initializes the 
        linkedlist by setting the head
        to None.
        Parameters:
            None
        Returns:
            None
        """
        self._head = None

    def update_count(self, word):
        """
        This function updates the count of a given 
        word in the linked list.
        Parameters:
            word: the word to be updated or 
            added in the linked list
        Returns:
            None
        """
        current = self._head
        while current != None:
            if current.word() == word:
                current.incr()
                return
            current = current.next()

        self.add(Node(word))

    # sort the nodes in the list
    # source: long problem for sorting a linked lists
    def sort(self):
        sorted_list = LinkedList()
        while self._head:
            current = self.remove_hd()
            if sorted_list._head is None or \
            current.count() >= sorted_list._head.count():
                sorted_list.add(current)
            else:
                prev = sorted_list._head
                while prev.next() and prev.next().count() > current.count():
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
    
    def get_nth_highest_count(self, n):
        """
        This function returns the count of the node at the 
        nth position in the linked list.
        Parameters:
            n: the position of the node to retrieve
        Returns:
            The count of the node at the nth 
            position in the linked list.
        """
        current = self._head
        index = 0
        while current and index < n:
            index += 1
            current = current.next()
        return current.count()

    def print_upto_count(self, n):
        """
        This method goes through the LinkedList
        and prints out all nodes that have a 
        count greater than or equal to n. 
        Parameters:
            n: an integer to be compared with each
            node's count
        Returns:
            None
        """
        words = []
        current = self._head
        while current:
            if current.count() >= n:
                words.append((current.count(), current.word()))
            current = current.next()
        for word in sorted(words, reverse=True):
            print(f"{word[1]} : {word[0]}")

    def __str__(self):
        string = ''
        current = self._head
        while current != None:
            string += f'{current.word()} : {current.count()}\n'
            current = current.next()
        return string

class Node:
    def __init__(self, word):
        """
        This function initalizes the Node with
        the word passed in and sets the count
        to 1 and the next to None. 
        Parameters:
            word: the word to make the node with
        Returns:
            None
        """
        self._word = word
        self._count = 1
        self._next = None
    
    def word(self):
        return self._word
    
    def count(self):
        return self._count
    
    def next(self):
        return self._next
    
    def set_next(self, target):
        self._next = target
    
    def incr(self):
        """
        This function increments the 
        count of the node by 1. 
        Parameters:
            None
        Returns:
            None
        """
        self._count += 1

    def __str__(self):
        return f"Word: {self._word}, Count: {self._count}"

def remove_punctuation(title_str):
    """
    This functions removes the punctuation 
    from a string
    Args:
        title_str: the string which 
        punctuation is removed from
    Returns:
        the string without punctuation
    """
    returned_str = ""
    for char in title_str:
        if char not in string.punctuation:
            returned_str += char
        else:
            returned_str += " "
    return returned_str

def handle_csv(filename):
    """
    This function reads in a CSV file and returns a 
    sorted LinkedList of cleaned words.
    Args:
        filename: the name of the CSV file to be read
    Returns:
        A sorted LinkedList of cleaned words from the CSV file.
    """
    infile = open(filename)
    csvreader = csv.reader(infile)
    clean_words_counter = LinkedList()
    for itemlist in csvreader:
        # ignore lines beginning with a '#'
        if not itemlist[0].startswith('#'):
            cleaned_list = []
            words_list = remove_punctuation(itemlist[4]).split()
            for word in words_list:
                if len(word) > 2:
                    cleaned_list.append(word.lower())
            for clean_word in cleaned_list:
                clean_words_counter.update_count(clean_word)
                    
    infile.close()
    clean_words_counter.sort()
    return clean_words_counter

def main():
    file_name = input()
    # create the linked list from the csv
    words_count_ll = handle_csv(file_name)
    n = int(input())
    count = words_count_ll.get_nth_highest_count(n)
    words_count_ll.print_upto_count(count)

if __name__ == "__main__":
    main()

