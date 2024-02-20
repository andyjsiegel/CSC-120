def ngram(arglist, startpos, length):
    if startpos + length > len(arglist):
        return []
    
    return arglist[startpos:startpos+length]

print(ngram([11,22,33,44,55], 0, 3))
print(ngram([11,22,33,44,55], 2, 3))
print(ngram([11,22,33,44,55], 3, 3))
print(ngram([11,22,33,44,55], -4, 3))
print(ngram([11,22,33,44,55], 1, 1))