def cv_match(sentence, pattern):
    words = sentence.split()
    words_that_match = []
    for word in words:
        if not len(word) == len(pattern):
            continue
        pattern_of_word = ""
        for char in word:
            if char not in "aeiouAEIOU":
                pattern_of_word += 'c'
            else:
                pattern_of_word += 'v'
        if pattern_of_word == pattern:
            words_that_match.append(word)
    
    return words_that_match
print(cv_match("Tim has a pet rat named Nip", "cvc"))

