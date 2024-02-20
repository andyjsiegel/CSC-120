def words_beginning_with(wordlist, head):
    matches = []
    if len(head) == 0:
        return wordlist
    for word in wordlist:
        if word[:len(head)] == head:
            matches.append(word)
    return matches