class Word: 
    def __eq__(self, other):
            # Sort the characters of both words
            sorted_self = sorted(self.word)
            sorted_other = sorted(other.word)

            # Check if the sorted words are equal
            return sorted_self == sorted_other
    def __init__(self, word):
        self._word = word
    def __str__(self):
	    return self._word.lower()
    
