def hash_prob(keys):
    def hash(key):
        return key % 7 
    def prob(key):
        return max(1, key // 7)
    for key in keys:
        print(hash(key), prob(key))
    

hash_prob([15,30,28,48,23])
