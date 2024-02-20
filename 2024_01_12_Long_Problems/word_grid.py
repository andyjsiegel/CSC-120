"""
    File: word_grid.py
    Author: Andy Siegel
    Course: CSC 120, Spring 2024
    Purpose: to generate a grid of random characters. 
"""

import random

def init():
    '''
    This function initializes a grid of a specified size 
    and seed value using inputs from the user.
    Args: 
        None
    Returns:
        None
    '''
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)
    return grid_size

def make_grid(grid_size):
    '''
    This function creates a grid of random characters 
    with a given size.
    Args:
        grid_size: the size of the grid
    Returns:
        a list containing a grid as a 2d list of random 
        characters with the given size
    '''
    grid_list = []
    for i in range(grid_size):
        grid_list.append([])
        for j in range(grid_size):
            sub_list = grid_list[i]
            letter = chr(random.randint(97, 122))
            sub_list.append(letter)
    return grid_list

def print_grid(grid):
    '''
    This function prints a grid by converting each row 
    into a string separated 
    by commas and then printing each row on a new line.
    Args:
        grid: a list of lists representing the grid
    Returns:
        None
    '''
    temp_list = []
    for row in grid:
        temp_list.append(','.join(row))
    print('\n'.join(temp_list))

def main():
    grid_size = init()
    grid_list = make_grid(grid_size)
    print_grid(grid_list)

main()