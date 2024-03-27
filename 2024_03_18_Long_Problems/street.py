"""
File: street.py
Author: Andy Siegel
Course: CSC 120, Spring 2024
Purpose: This program takes in an input from the user in a specific format and 
    generates an ASCII representation of a street with Building, EmptyLot, 
    and Park objects using many recursive functions.  
"""
def replace_string(string, old_str, new_str):
    """
    This function takes in a string, an old string, and a new string, and 
    replaces all instances of the old string with the new string in the 
    original string. It uses recursion to iterate through the original 
    string and replace each instance of the old string with the new string.
    Args:
        string
        old_str
        new_str
    Returns:
        The string with the characters replaced.
    """
    if not string:
        return ''
    else:
        if string[0] == old_str:
            return new_str + replace_string(string[1:], old_str, new_str)
        else:
            return string[0] + replace_string(string[1:], old_str, new_str)
        
def get_height_of_street(street):
    """
    This function takes in a list of urban elements and returns the height of 
    the tallest element in the list using recursion. 
    Args:
        street
    Returns:
        the tallest height
    """
    if len(street) == 1:
        return street[0].height()
    else:
        max_rest = get_height_of_street(street[1:])
        if street[0].height() > max_rest:
            return street[0].height()
        else:
            return max_rest

def get_width_of_street(street):
    """
    This function takes in a list of urban elements and returns the 
    sum of the all of the widths of the elements using recursion.
    Args:
        street
    Returns:
        the sum of all the widths
    """
    if len(street) < 2:
        return street[0].width()
    return street[0].width() + get_width_of_street(street[1:])

def print_street_at_height(street, height, first_run):
    """
    This function prints the street at a given height, with the option to add 
    a vertical bar at the beginning if it is the first run for the vertical 
    borders of the art. It recursively calls itself to print the remaining 
    parts of the street.
    Args:
        street
        height
        first_run
    Returns:
        None
    """
    if first_run:
        print('|', end='')
    if len(street) < 2:
        print(street[0].at_height(height), end = '|\n')
    else:
        print(street[0].at_height(height), end='')
        print_street_at_height(street[1:], height, False)

def get_border(width):
    """
    This function takes in a width parameter and returns a string that 
    represents a border with the specified width, consisting of a 
    '+' character on each end and '-' characters in between.
    Args:
        width
    Returns:
        the horizontal border as a string
    """
    return '+' + '-' * width + '+'

def print_street(street, height, first_run):
    """
    This function prints a street given a height, and recursively prints the 
    street at decreasing heights until reaching 0. It also prints a border at 
    the top and bottom to add to the art using the first_run variable to not
    print it more than once.
    Args:
        street
        height
        first_run
    Returns:
        None
    """
    if first_run:
        print(get_border(get_width_of_street(street)))
    if height == 0:
        print_street_at_height(street, 0, True)
        print(get_border(get_width_of_street(street)))
    else:
        print_street_at_height(street, height, True)
        print_street(street, height-1, False)
    
def urbanify(string):
    """
    This function takes in a string and splits it into attributes. 
    Depending on the first letter of the string, it creates and returns an 
    EmptyLot, Building, or Park object with the specified width and other 
    attributes.
    Args:
        string
    Returns:
        an EmptyLot, Building, or Park object
    """
    attributes = string.split(':', 1)[1].split(',')
    if 'e' in string:
        width = int(attributes[0])
        trash = attributes[1]
        return EmptyLot(width, trash)
    elif 'b' in string:
        width = int(attributes[0])
        height = int(attributes[1])
        brick = attributes[2]
        return Building(width, height, brick)
    elif 'p' in string:
        width = int(attributes[0])
        foliage = attributes[1]
        return Park(width, foliage)

def urbanify_elements(input_list):
    """
    This function takes in a list generated from a string split on whitespace.
    Using recursion, it loops through the list and calls urbanify() on them. 
    Args:
        input_list
    Returns:
        a list of Park, Building, and/or EmptyLot objects.
    """
    if len(input_list) == 1:
        return [urbanify(input_list[0])]
    else:
        return [urbanify(input_list[0])] + urbanify_elements(input_list[1:])
    
class Park:
    """
    This class represents a park in ASCII art.
    """
    def __init__(self, width, foliage):
        """
        This function initializes a Park object with the given width and 
        foliage parameters, assigning them to the corresponding attributes 
        of the object.
        Parameters:
            width
            foliage
        Returns:
            None
        """
        self._width = width
        self._foliage = foliage

    def width(self):
        return self._width
    
    def height(self):
        # height of a Park is constant
        return 5
    
    def get_width_from_height(self, height):
        """
        This function takes in a height value and returns a corresponding 
        width value based on a predefined dictionary. Parks are always odd 
        in width, and always have a height of 5. At h=4, the width of the tree
        is 1 for 1 leaf. At h=3, there's 3 leaves. At h=2, there are 5 leaves.
        At h<2, there is a trunk represented by '|' with a width of 1. 
        Parameters:
            height
        Returns:
            The width from the height converted via the dictionary
        """
        return {4: 1, 3: 3, 2: 5, 1: 1, 0:1}[height]

    def at_height(self, height):
        """
        This method takes in a height parameter and returns a string 
        representation of the Park based on the height. If the height is 
        greater than 4, it returns an empty string. Otherwise, it calculates 
        the width of the string based on the height and returns a string with 
        the appropriate number of spaces.
        Parameters:
            height
        Returns:
            The string representing the park at the given height.
        """
        char = self._foliage
        if height > 4:
            return ' ' * self._width
        else:
            if height < 2:
                char = '|'
            width_sep = self.get_width_from_height(height)
            half_width = (self._width - width_sep) // 2
            return ' ' * half_width + char * width_sep + ' ' * half_width
        
class Building:
    """
    This class represents a Building in ASCII art.
    """
    def __init__(self, width, height, brick):
        """
        This method creates a Building object with specified width, height, and 
        brick material, and assigns them to the corresponding attributes of the 
        object.
        Parameters:
            width
            height
            brick
        Returns:
            None
        """
        self._width = width
        self._height = height
        self._brick = brick

    def at_height(self, height):
        """
        This method creates the string representation of the building at the 
        height. If the given height is greater than the building's height, it
        returns a string of spaces with the length equal to the width.
        Otherwise, it will return a string of the brick material with the 
        length equal to the width.
        Parameters:
            height
        Returns:
            a string representation of the building at the height. 
        """
        if height >= self._height:
            return ' ' * self._width
        return self._brick * self._width
    
    def height(self):
        return self._height
    
    def width(self):
        return self._width

class EmptyLot:
    """
    This class represents an Empty Lot that fills up with trash in ASCII art. 
    """
    def __init__(self, width, trash):
        """
        This method initializes an object with a given width and trash string, 
        replacing any underscores in the trash string with spaces using the 
        recursive function replace_string() and stores it in the object's 
        trash attribute.
        Parameters:
            width
            trash
        Returns:
            null
        """
        self._width = width
        trash_str = (trash * (self._width // len(trash) + 1))[:self._width]
        self._trash = replace_string(trash_str, '_',' ')

    def at_height(self, height):
        """
        This method checks if the given height is equal to 0 and if so, 
        returns the trash attribute of the object. Otherwise, it returns a 
        string of empty spaces with a length equal to the width attribute.
        Parameters:
            height
        Returns:
            A string representation of the EmptyLot given the height. 
        """
        if height == 0:
            return self._trash
        return ' ' * self._width
    
    def height(self):
        return 1
    def width(self):
        return self._width

def main():
    street_input = input("Street: ")
    street = urbanify_elements(street_input.split())
    height = get_height_of_street(street)
    print_street(street, height, True)

if __name__ == "__main__":
    main()