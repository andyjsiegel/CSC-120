"""
File: friends.py
Author: Andy Siegel
Course: CSC 120, Spring 2024
Purpose: This program imports the LinkedList
    and Node classes from linked_list.py to 
    handle the creation of a LinkedList that
    represents a list of friends to find mutual
    friends. 
"""
from linked_list import *

def handle_file(filename):
    """
    This function takes in a file name and
    processes it to create a linked list of
    people and their friends ensuring that 
    symmetric relations are created.
    Args:
        filename: the name of the file
    Returns:
        main_list: a LinkedList
    """
    file = open(filename, 'r')
    main_list = LinkedList()
    for line in file:
        line_info = line.strip().split()
        first_name, second_name = line_info[0], line_info[1]

        main_list.make_friends(first_name, second_name)
        main_list.make_friends(second_name, first_name)

    file.close()
    return main_list

def main():
    file_name = input('Input file: ')
    main_list = handle_file(file_name)

    name1 = input('Name 1: ')
    name2 = input('Name 2: ')
    
    exists_name1, name1_node = main_list.exists(name1)
    exists_name2, name2_node = main_list.exists(name2)
    if not exists_name1:
        print("ERROR: Unknown person " + name1)
    elif not exists_name2:
        print("ERROR: Unknown person " + name2)
    else:
        name1_friends = name1_node.get_friends()
        name2_friends = name2_node.get_friends()
        mutuals = name1_friends.intersection(name2_friends)
        mutuals.sort()
        if not mutuals.is_empty():
            print("Friends in common:")
            print(mutuals)

if __name__ == "__main__":
    main()