# data1 = [4, 'carted','at','barn','elephant','death', 1,3,2]
# data2 = sorted(data1)
# assert data2[0] <= data2[1]
# print("test passed")

def first_matches_last(L):
    return [str for str in L if len(str) == 0 or (len(str) > 0 and str[0] == str[-1])]


# print(first_matches_last(['radar','cat','h','Gyatt dayum','palindromep','']))

class Word: 
    def __init__(self, word): 
        self._word = word 
    def __eq__(self, other): 
        return (len(self._word) == len(other._word) and set(self._word) == set(other._word))

w1 = Word("post") 
w2 = Word("stop") 
print(w1 == w2) 
w1 = Word("peep") 
w2 = Word("keep") 
print(w1 == w2) 
