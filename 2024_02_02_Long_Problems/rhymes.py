"""
File: rhymes.py
Author: Andy Siegel
Course: CSC 120, Spring 2024
Purpose: This program takes in a list of words with pronounciations and
then takes input from the user and finds all words that rhyme with the 
user's input word. 
"""
def get_prim_stress_index(phoneme_list):
    """
    This function returns the index of the first 
    phoneme with primary stress in the given list.
    Args:
        phoneme_list: list of phonemes
    Returns:
        index of the first phoneme with primary stress, 
        or None if no such phoneme exists in the list.
    """
    for phoneme in phoneme_list:
        if '1' in phoneme:
            return phoneme_list.index(phoneme)

def align_lists(list1, list2):
    """
    This function aligns two lists of phonemes by inserting None to ensure
    they have the same length and primary stress index for rhyme detection.
    Args:
        list1: the first list of phonemes
        list2: the second list of phonemes
    Returns:
        first_list: the first list with added None values if needed
        second_list: the second list with added None values if needed
        final_prim_stress: the index of the 
        primary stress phoneme for rhyme detection
    """
    first_list, second_list = list(list1), list(list2)
    prim_stress_index1 = get_prim_stress_index(first_list)
    prim_stress_index2 = get_prim_stress_index(second_list)
    # if one of the words does not have a primary stress, it cannot rhyme
    if prim_stress_index1 is None or prim_stress_index2 is None: 
        return False
    final_prim_stress = prim_stress_index1
    if prim_stress_index1 > prim_stress_index2:
        final_prim_stress = prim_stress_index1
        while True:
            if prim_stress_index1 >= len(second_list):
                second_list.insert(0, None)
            elif '1' not in second_list[prim_stress_index1]:
                second_list.insert(0, None)
            else:
                break
    elif prim_stress_index1 < prim_stress_index2:
        final_prim_stress = prim_stress_index2
        while True:
            if prim_stress_index2 >= len(first_list):
                first_list.insert(0, None)
            elif '1' not in first_list[prim_stress_index2]:
                first_list.insert(0, None)
            else:
                break
    diff = abs(len(first_list) - len(second_list))
    # add None to shorter list to ensure the lengths match
    if len(first_list) < len(second_list): 
        first_list.extend([None] * diff)
    else: 
        second_list.extend([None] * diff)

    return first_list, second_list, final_prim_stress

def check_for_rhymes(phoneme_list1, phoneme_list2, prim_stress_index):
    """
    This function checks if two words have the same primary stressed 
    syllable and returns True if they do, False otherwise.
    Args:
        phoneme_list1: list of phonemes for the first word
        phoneme_list2: list of phonemes for the second word
        prim_stress_index: index of the primary stressed 
        syllable in the phoneme lists
    Returns:
        True if the words meet all the conditions to rhyme, False otherwise.
    """
    p_s_i = prim_stress_index
    
    # if the primary stress doesn't match, the words do not rhyme.
    if phoneme_list1[p_s_i] != phoneme_list2[p_s_i]:
        return False
    # if the phoneme preceding the primary stress is the same, 
    # the words do not rhyme.
    if phoneme_list1[p_s_i-1] == phoneme_list2[p_s_i-1]:
        return False
    # if all the phonemes following the primary stress aren't the same,
    # the words do not rhyme. 
    if phoneme_list1[p_s_i:] != phoneme_list2[p_s_i:]:
        return False
    
    return True


def organize_dict(pronounciations_file):
    """
    This function creates a dictionary of words and their
    corresponding phonemes from a pronunciation file.
    Args:
        pronounciations_file: the pronunciation file to be organized
    Returns:
        a dictionary with words as keys and a 2d list of 
        their corresponding pronounciations and phonemes as values
    """
    file = open(pronounciations_file, 'r')
    pronounciation_dict = {}
    for line in file:
        # words are separated from by phonemes by two spaces
        word = line.split('  ')[0]
        # phonemes are the rest of the line -- remove \n and 
        # then split on single space to get each phoneme
        pronounciations = line.split('  ')[1].strip('\n')
        phonemes_list = pronounciations.split(' ')
        # if the word isnt in the dictionary, add it with 
        # the phonemes as a 2d list otherwise, add the list 
        # of phonemes to the 2d list. 
        if word not in pronounciation_dict:
            pronounciation_dict[word] = [phonemes_list]
        else:
            pronounciation_dict[word].append(phonemes_list)
    file.close()
    return pronounciation_dict

def main():
    file_name = input()
    pronounciations_dict = organize_dict(file_name)
    user_word = input().upper()
    user_word_pronounciations = pronounciations_dict[user_word]
    rhymes_list = []
    for word_in_dict, phonemes_2d_list in pronounciations_dict.items():
        for phoneme_sublist in phonemes_2d_list:
            for user_word_phonemes in user_word_pronounciations:
                result = align_lists(phoneme_sublist, user_word_phonemes)
                # align_lists() either returns a tuple, or False
                if result:
                    first_list, second_list, prim_stress_index = result
                    if check_for_rhymes(
                        first_list, second_list, prim_stress_index
                    ):
                        rhymes_list.append(word_in_dict)
                # if result is false, words do not rhyme 
                # and no code needs to be executed
    
    for word in sorted(rhymes_list):
        print(word)
                

main()