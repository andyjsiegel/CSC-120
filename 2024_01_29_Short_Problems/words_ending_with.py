def words_ending_with(wordlist, tail):
    matches = []
    if len(tail) == 0:
        return wordlist
    for word in wordlist:
        if word[-len(tail):] == tail:
            matches.append(word)
    return matches