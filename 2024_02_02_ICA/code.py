class Word: 
    def __init__(self, text): 
    # store a “clean” version of the string text 
    # strip off punctuation and convert to lowercase  
        self._word = self.clean_word(text)
    def __str__(self): 
        return "Word(" + self._word + ")" 
    def clean_word(self, text):
        return text.strip(".!:;,?-").lower()

a = Word("-Hello!!") 
print(str(a)) # Word(hello)

