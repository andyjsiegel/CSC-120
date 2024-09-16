def char_countv2(text):
    cdict = {} 
    for char in text: 
        if char in cdict: 
            cdict[char] = cdict[char] + [1] 
        else: 
            cdict[char] = [1] 
    return cdict

assert char_countv2("to be or not to be") == {'t': [1, 1, 1], 'o': [1, 1, 1, 1], ' ': [1, 1, 1, 1, 1], 'b': [1, 1], 'e': [1, 1], 'r': [1], 'n': [1]}

class Dictionary:
    pass

def char_countv3(text):
    d = Dictionary(len(text))
    for char in text: 
        if char in d: 
            d.put(char, d.get(char) + [1])
        else: 
            d.put(char, [1])
    return d


