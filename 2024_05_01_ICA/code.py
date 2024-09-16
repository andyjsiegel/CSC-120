def next_words(w1, words_list):
    valid_returns = []
    for word in words_list:
        diff = sum(a != b for a, b in zip(w1, word))
        if len(word) == len(w1) and diff == 1:
            valid_returns.append(word)
    return valid_returns

# # Test cases for the next_words function
# words_list = ["apple", "apply", "orange", "pear", "peach"]

# w1 = "apple"
# print(next_words(w1, words_list))

# w1 = "pear"
# print(next_words(w1, words_list))

# w1 = "orange"
# print(next_words(w1, words_list))

# w1 = "grange"
# print(next_words(w1, words_list))

# w1 = "apply"
# print(next_words(w1, words_list))

def dist(w1: str, w2: str) -> list:
    return {w1.index(a): a != b for a,b in zip(w1,w2)}

print(dist('orange','grange'))

class CharStack:
    def __init__(self):
        self._stack = ""

    def push(self, char):
        self._stack += char

    def pop(self):
        if not self.is_empty():
            char = self._stack[-1]
            self._stack = self._stack[:-1]
            return char

    def swap(self):
        if len(self._stack) >= 2:
            self._stack = self._stack[:-2] + self._stack[-1] + self._stack[-2]

    def is_empty(self):
        return not bool(self._stack)

    def __str__(self):
        return self._stack

cs = CharStack()
cs.push('p')
cs.push('a')
cs.push('n')
cs.push('s')
print(cs)   # snap
cs.swap()
cs.pop()    # 'n'
print(cs)   # sap
cs.is_empty()   # False



