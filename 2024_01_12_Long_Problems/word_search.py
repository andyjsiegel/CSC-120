def get_word_list(filename):
    """
    This function takes in a filename and returns a list of words 
    from the file, 
    with each word stripped of new line characters and 
    converted to lowercase.
    Args:
        filename: the name of the file to be read
    Returns:
        a list of words from the file, with each word converted to 
        lowercase and stripped of new line characters
    """
    f = open(filename, 'r')
    word_list = f.readlines()
    for i in range(len(word_list)):
        word_list[i] = word_list[i].strip('\n').lower()
    
    f.close()
    return word_list

def read_letters_files(the_grid):
    """
    This function reads a file containing letters in a grid pattern and 
    returns a 2d list of the letters.
    Args:
        the_grid: the file containing the letters
    Returns:
        a 2d list of the letters in the file (each sub-array represents rows)
    """
    f = open(the_grid, 'r')
    letters = []
    for line in f.readlines():
        letters.append(line.strip('\n').split(' '))
    f.close()
    return letters 

def flip_grid(letter_grid):
    """
    This function flips a 2d list which represents a grid -- the sub-arrays 
    become columns rather than rows
    Args:
        letter_grid: the 2d array which represents the grid
    Returns:
        a 2d list of the letters in the file 
        (each sub-array represents columns)
    """
    flipped_grid = []
    for i in range(len(letter_grid)):
        column = []
        for j in range(len(letter_grid)):
            column.append(letter_grid[j][i])
        flipped_grid.append(column)
    return flipped_grid

def get_diagonals(letter_grid):
    """
    This function returns a 2d list of all diagonals in a letter grid.
    Args:
        letter_grid: the 2d array which represents the grid
    Returns:
        a 2d list of all diagonals in the letter grid 
        (each sub-array is a diagonal)
    """
    # GET ALL DIAGONALS (MIDDLE TO END)
    diagonals = []
    for i in range(1, len(letter_grid)):
        diagonal = []
        for j in range(len(letter_grid) - i):
            diagonal.append(letter_grid[i + j][j])
        diagonals.append(diagonal)

    diagonals = diagonals[::-1] 
    # FLIP ORDER SO LIST SIZE BUILDS UP AND THEN BACK DOWN 
    # SMALLEST LISTS AT THE ENDS
    
    # GET OTHER DIAGONALS (BOTTOM RIGHT TO MIDDLE)
    for i in range(len(letter_grid)):
        diagonal = []
        for j in range(len(letter_grid)):
            if i + j < len(letter_grid):
                diagonal.append(letter_grid[j][i+j])
        diagonals.append(diagonal)

    return diagonals

def search_horizontally(letter_grid):
    """
    This function returns a list of all 3+ 
    letter substrings in the letter grid.
    These substrings are in the horizontal directions.
    Args:
        letter_grid: the 2d array which represents the grid
    Returns:
        a list of horizontal 3+ letter substrings in the letter grid.
    """
    substrings = []
    for row in letter_grid:
        for j in range(3, len(row)+1):
            substr_row_list = get_substrings(row, j)
            for substr in substr_row_list:
                substrings.append(substr)

    # SEARCH HORIZONTALLY R => L
    for row in letter_grid:
        for j in range(3, len(row)+1):
            substr_row_list = get_substrings(row[::-1], j)
            for substr in substr_row_list:
                substrings.append(substr)  
    
    return substrings

def search_vertically(flipped_grid):
    """
    This function returns a list of all 3+ 
    letter substrings in the letter grid.
    These substrings are in the vertical directions.
    Args:
        letter_grid: the 2d array which represents the grid
    Returns:
        a list of vertical 3+ letter substrings in the letter grid.
    """
    substrings = []

    # SEARCH TOP TO BOTTOM
    for column in flipped_grid:
        for j in range(3, len(flipped_grid)+1):
            substr_row_list = get_substrings(column, j)
            for substr in substr_row_list:
                substrings.append(substr)   

    # SEARCH BOTTOM TO TOP
    for column in flipped_grid:
        for j in range(3, len(flipped_grid)+1):
            substr_row_list = get_substrings(column[::-1], j)
            for substr in substr_row_list:
                substrings.append(substr)  
    
    return substrings

def search_diagonally(diagonals):
    """
    This function returns a list of all 3+ 
    letter substrings in the letter grid.
    These substrings are in the diagonal top 
    left to bottom right direction.
    Args:
        letter_grid: the 2d array which represents the grid
    Returns:
        a list of diagonal 3+ letter 
        substrings in the letter grid.
    """
# SEARCH DIAGONALS TOP LEFT TO RIGHT BOTTOM
# [2:-2] excludes the diagonals of 
# length 1 and 2 (invalid words)
    substrings = []
    for diag in diagonals[2:-2]: 

        for j in range(3, len(diagonals[2:-2])+1):
            substr_row_list = get_substrings(diag, j)
            for substr in substr_row_list:
                substrings.append(substr)  

    return substrings

def find_all_potential_words(letter_grid):
    """
    This function combines all searching functions 
    to combine together a list of 
    all 3+ letter substrings in all directions
    Args:
        letter_grid: the 2d array which represents the grid
    Returns:
        a list of all 3+ letter substrings in the letter grid.
    """
    substrs_list = search_horizontally(letter_grid) 
       
    flipped_grid = flip_grid(letter_grid)

    substrs_list = substrs_list + search_vertically(flipped_grid)

    diagonals = get_diagonals(letter_grid)    
    
    substrs_list = substrs_list + search_diagonally(diagonals)
    
    return substrs_list
    
def get_substrings(characters, n):
    """
    This function takes in a list of characters and 
    returns all consecutive substrings of length n
    Args:
        characters: a list of characters
        n: the length of the substrings that should be returned
    Returns:
        A list of all the substrings of length n
    """
    substr_list = []
    for index in range(n, len(characters)+1): 
        next_string = ''.join(characters[index-n:index]) 
        substr_list.append(next_string)
    return substr_list

def occurs_in(substr, word_list):
    """
    This function checks if a given substring is in a list of words.
    Args:
        substr: a substring
        word_list: a list of words
    Returns:
        a boolean of whether the substring is in the word_list
    """
    return substr in word_list

def print_words(words):
    """
    This function takes in a list of words, sorts them 
    alphabetically, and prints them one by one. 
    Args:
        a list of words
    Returns:
        None
    """
    words.sort()
    for word in words:
        print(word)

def main():
    words_list = input()
    the_grid = input()
    letter_grid = read_letters_files(the_grid)
    substrs_list = find_all_potential_words(letter_grid)
    
    word_list = get_word_list(words_list)
    real_words = []
    for substring in substrs_list:
        if occurs_in(substring, word_list):
            real_words.append(substring)

    print_words(real_words)

main()