def kth_elements(L, k):
    return [L[i] for i in range(len(L)) if i % k == 0]

print(kth_elements([1,2,3,4], 2))