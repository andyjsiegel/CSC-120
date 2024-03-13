def get_even_positions(ints):
    if len(ints) < 1:
        return []
    return [ints[0]] + get_even_positions(ints[2:])

# print(get_even_positions([2,6,5,33,8]))

def max_l(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        max_rest = max_l(alist[1:])
        if alist[0] > max_rest:
            return alist[0]
        else:
            return max_rest

my_list = [3, 7, 2, 10, 5]
# print(max_l(my_list)) # 10
# full list passed in, len > 1 so else activates
# max_rest is initalized finding the max of the rest of the list. eventually, list gets down to the final element in this case 5
# going up one recursive call, 5 < 10 so 10 is returned, then 10 > all other elements going back up to the initial call. 

def maxmin(alist):
    if len(alist) == 1:
        return alist[0], alist[0]
    max_rest, min_rest = maxmin(alist[1:])
    
    if alist[0] > max_rest:
        max_val = alist[0]
    else:
        max_val = max_rest
        
    if alist[0] < min_rest:
        min_val = alist[0]
    else:
        min_val = min_rest
    
    return (max_val, min_val)

# basically an expanded version of the max_l function
lst = [3, 1, 7, 4, 6, 2, 8, 5]
# print(maxmin(lst))

def flatten(alist):
    if len(alist) == 0:
        return []
    if type(alist[0]) == int:
        return [alist[0]] + flatten(alist[1:])
    else:
        return flatten(alist[0]) + flatten(alist[1:])

# print(flatten([[2, 4, 6], [10, [100, 200], 20], [[66], [[77, 88]], 99]]) )



def partition(alist, a):
    if len(alist) == 1:
        return [], [alist[0]]
    
    less_rest, greater_rest = partition(alist[1:], a)

    if alist[0] > a:
        greater_rest = [alist[0]] + greater_rest
        
    if alist[0] <= a:
        less_rest = [alist[0]] + less_rest

    return ( less_rest, greater_rest)

print(partition([1,7,5,6,3,4,2,9], 6))




