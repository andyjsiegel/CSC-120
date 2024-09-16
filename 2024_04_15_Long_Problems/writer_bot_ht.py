"""
File: writer_bot_ht.py
Author: Andy Siegel
Course: CSC 120, Spring 2024
Purpose: This program creates random text using a Markov chain. It reads a text
    file, builds the chain using a specified n-gram size, and generates text in
    10-random_suffix rows. Users input the source file, prefix length, size of
    the hash table an number of  words to generate. The output is a 
    sequence derived from the input text and Markov chain logic.
    """

import sys

class Hashtable:
    """
    This class implements a hashtable data type given a size.
    """
    def __init__(self, size):
        """
        This function initializes the hashtable with a specified size and
        creates a list of pairs to represent the hashtable with the size.
        Parameters:
            size
        Returns:
            None
        """
        self._pairs = [None] * size
        self._size = size

    def put(self, key, value):
        """
        This method takes in a key and value, calculates an index based on the
        key using the private method _hash(), and then inserts the key-value
        pair into a list at that index, using linear probing to handle
        collisions.
        Parameters:
            key
            value
        Returns:
            None
        """
        index = self._hash(key)
        while self._pairs[index] is not None:
            index = (index - 1) % self._size
        self._pairs[index] = [key, value]

    def get(self, key):
        """
        This method searches for a specific key in a hash table and returns the
        corresponding values if found, or None if the key is not present. It
        uses a while loop to iterate through the table and a hashing function
        to determine the index of the key. It does not iterate through the 
        entire table; if it runs into an empty slot, it returns None because 
        the value is not in the table due to the nature of linear probing and
        clusters.
        Parameters:
            key
        Returns:
            return values or None
        """
        index = self._hash(key)
        while self._pairs[index] is not None:
            stored_key, values = self._pairs[index]
            if stored_key == key:
                return values
            index = (index - 1) % self._size
        return None

    def __contains__(self, key):
        """
        This method checks if the given key is present in the hash table by
        using the same logic as the get() method, but returns a boolean instead
        of the value. 
        Parameters:
            key
        Returns:
            True or False
        """
        index = self._hash(key)
        while self._pairs[index] is not None:
            stored_key, value = self._pairs[index]
            if stored_key == key:
                return True
            index = (index - 1) % self._size 
        return False

    def __str__(self):
        return str(self._pairs)

    def _hash(self, key):
        """
        This function takes in a key and uses a hashing algorithm to generate a
        unique index value for that key, which is then returned.
        Parameters:
            key
        Returns:
            hash_index
        """
        hash_value = 0
        for char in key:
            hash_value = 31 * hash_value + ord(char)
        hash_index = hash_value % self._size
        return 



import random
# constant for seeding the random number generator
SEED = 8
# constant character to represent a null word.
NONWORD = "@"

def read_file(filename):
    """
    This function takes in a filename as a parameter, opens the file, reads its
    contents, and returns a list of words from the file. It also closes the
    file after reading.
    Args:
        filename: name of the file
    Returns:
        text: list of words in the file
    """
    file = open(filename, 'r')
    # turn text file into a list of words
    text = file.read().replace('\n', ' ').split()
    file.close()
    return text

def build_markov_chain(text, size, n):
    """
    This function builds a Markov chain data structure using a given text and
    specified parameters for size and n. It iterates through the text, adding
    each word to the chain and updating the prefix for the next iteration.
    Args:
        text: the text from the file
        size: the size of the hashtable
        n: the length of the prefix
    Returns:
        markov_chain: the markov chain made with the hashtable.
    """
    markov_chain = Hashtable(size)
    prefix = ((NONWORD + ' ') * n).strip()
    
    for word in text:
        if prefix not in markov_chain:
            markov_chain.put(prefix, [word])
        else:
            suffixes = markov_chain.get(prefix)
            suffixes.append(word)
        # move prefix down 1 word
        temp_list = prefix.split(' ')[1:]
        temp_list.append(word)
        prefix = ' '.join(temp_list)
    
    return markov_chain

def generate_text(markov_chain, n, num_words):
    """
    This function generates a random text of a specified length using a given 
    Markov chain and a prefix length. It iterates through the Markov chain, 
    randomly selecting suffixes to add to the generated text until the desired 
    number of words is reached.
    Args:
        markov_chain: a markov chain represented by the Hashtable class
        n: the length of the prefix
        num_words: number of words to have in the text
    Returns:
        generated_text: the text made via the markov chain
    """
    prefix = ((NONWORD + ' ') * n).strip()
    generated_text = []
    
    for i in range(num_words):
        # avoid IndexError by exiting the loop
        if prefix not in markov_chain:
            break
        suffixes = markov_chain.get(prefix)
        random_index = 0
        # only use random if there are multiple to choose from
        if len(suffixes) > 1:
            random_index = random.randint(0, len(suffixes) - 1)

        random_suffix = suffixes[random_index]
        generated_text.append(random_suffix)
        # move prefix down one element 
        temp_list = prefix.split(' ')[1:]
        temp_list.append(str(random_suffix))
        prefix = ' '.join(temp_list)
    
    return generated_text

def print_output(generated_text):
    """
    This function takes in a string of generated text and 
    prints it out in rows of 10 words each, separated by spaces.
    Args:
        generated_text
    Returns:
        None
    """
    rows = []
    for i in range(0, len(generated_text), 10):
        rows.append(generated_text[i:i+10])
    for row in rows:
        print(" ".join(row))
    

def main():
    random.seed(SEED)

    source_file = input()
    hashtable_size = int(input())
    prefix_size = int(input())
    num_words = int(input())

    if prefix_size < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)
    if num_words < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)

    source_text = read_file(source_file)

    markov_chain = build_markov_chain(source_text, hashtable_size, prefix_size)

    random_text = generate_text(markov_chain, prefix_size, num_words)

    print_output(random_text)

if __name__ == "__main__":
    main()