def mystery_one(data): 
  for i in range(len(data)): 
    for j in range(len(data)-1): 
        if data[j] > data[j+1]: 
            data[j],data[j+1] = data[j+1],data[j] 

def have_two_greater(alist):
    result = []
    for i in range(len(alist)):
        count = 0
        for j in range(len(alist)):
            if i != j and alist[j] > alist[i]: 
                count += 1
                if count >= 2:
                    result.append(alist[i])
                    break
    return result

# print(have_two_greater([1, 2, 3, 4, 5, 6]))  # [1,2,3,4]

def second_largest(alist):
    return sorted(alist)[-2]

print(second_largest([2,5,1,3,6,4]))