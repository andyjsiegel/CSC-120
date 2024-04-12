"""
File: writer_bot.py
Author: Andy Siegel
Course: CSC 120, Spring 2024
Purpose: This program creates random text using a Markov chain. It reads a text
    file, builds the chain using a specified n-gram size, and generates text in
    10-word rows. Users input the source file, prefix length, and number of 
    words to generate. The output is a probabilistic word sequence derived 
    from the input text and Markov chain logic.
    """

import random
# constant for seeding the random number generator
SEED = 8
# constant for the non-word
NONWORD = " "

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

def build_markov_chain(text, n):
    """
    This function takes in a text and an integer n, and builds a Markov chain 
    based on the text and the specified n-gram size. It then returns the 
    Markov chain as a dictionary.
    Args:
        text: a list of words
        n: an integer
    Returns:
        markov_chain: a dictionary of prefixes and suffixes
    """
    markov_chain = {}
    prefix = tuple([NONWORD] * n)
    
    for word in text:
        if prefix not in markov_chain:
            markov_chain[prefix] = []
        markov_chain[prefix].append(word)
        # move prefix down 1 word
        prefix = (prefix + (word,))[1:]
    
    return markov_chain

def generate_text(markov_chain, n, num_words):
    """
    This function generates a random text of a specified length using a given 
    Markov chain and a prefix length. It iterates through the Markov chain, 
    randomly selecting suffixes to add to the generated text until the desired 
    number of words is reached.
    Args:
        markov_chain: a markov chain represented by a dictionary
        n: the length of the prefix
        num_words: number of words to have in the text
    Returns:
        generated_text: the text made via the markov chain
    """
    prefix = tuple([NONWORD] * n)
    generated_text = []
    
    for i in range(num_words):
        # avoid IndexError by exiting the loop
        if prefix not in markov_chain:
            break
        suffixes = markov_chain[prefix]
        random_index = 0
        # only use random if there are multiple to choose from
        if len(suffixes) > 1:
            random_index = random.randint(0, len(suffixes) - 1)

        random_suffix = suffixes[random_index]
        generated_text.append(random_suffix)
        # move prefix down one element 
        prefix = (prefix + (random_suffix,))[1:]
    
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
    n = int(input())
    num_words = int(input())

    source_text = read_file(source_file)
    markov_chain = build_markov_chain(source_text, n)

    random_text = generate_text(markov_chain, n, num_words)

    print_output(random_text)

if __name__ == "__main__":
    main()
