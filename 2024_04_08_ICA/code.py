def partition(alist, pivot):
    list1, list2 = [], []
    for value in alist:
        if value <= pivot:
            list1.append(value)
        else:
            list2.append(value)
    return list1, list2

# print(partition([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 3))
# print(partition([-3, 1, -4, 0, 5, -9, 2, 6, 4, 3, 0], 0))
# print(partition([2, 2, 1, 1, 3, 3, 2, 4], 2))
# print(partition([], 5))
# print(partition([8, 9, 10, 12, 11], 5))

class Dictionary:
    def __init__(self, size):
        self._pairs = [None] * size
    
    def _hash(self, k):
        return len(k) % len(self._pairs)
    
    def put(self, k, v):
        index = self._hash(k)
        self._pairs[index] = [k,v] 

    def get(self, k):
        index = self._hash(k)
        return self._pairs[index][1]

        
    
