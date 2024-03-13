def bin_search(alist, item):
    if len(alist) == 0:
        return False
    elif item == alist[0]:
        return True
    return bin_search(alist[1:], item)

# Test cases for binary search function

assert bin_search([1, 2, 3, 4, 5], 3) == True  # Item present in the list
assert bin_search([1, 2, 3, 4, 5], 6) == False  # Item not present in the list
assert bin_search([], 5) == False  # Empty list
assert bin_search([1, 2, 3, 4, 5], 1) == True  # Item present at the beginning

def sum_col(grid, col):
    if grid == []:
        return 0
    else:
        return grid[0][col] + sum_col(grid[1:], col)

# Test cases for sum column function

assert sum_col([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == 15
assert sum_col([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]], 0) == -12
assert sum_col([], 0) == 0
assert sum_col([[10], [20], [30]], 0) == 60

def slice_each_inner_list(a_2d_list, pos):
    if a_2d_list == []:
        return 0
    return a_2d_list[0][pos] + slice_each_inner_list(a_2d_list[1:], pos+1)

def sum_diag(grid):
    return slice_each_inner_list(grid, 0)

def zip(a,b):
    shorter_list = []
    if len(a) < len(b):
        shorter_list = a
    else: 
        shorter_list = b
    if shorter_list == []:
        return []
    else:
        return [(a[0], b[0])] + zip(a[1:], b[1:])
    
assert zip([1,2,3],[4,5,6]) == [ (1,4), (2,5), (3, 6) ] 
assert zip([1,2,3,4,5],['a','b','c','d','e']) == [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')] 
assert zip([2,4,6], ['fall','leaves']) == [(2, 'fall'), (4, 'leaves')]
assert zip([], [4,5,6]) == []

def zip_helper(a,b, result):
    if a == [] or b == []:
        return result
    result += [( a[0], b[0] )]
    return zip_helper(a[1:], b[1:], result)

def zip2(a,b):
    return zip_helper(a,b,[])

assert zip2([1,2,3],[4,5,6]) == [ (1,4), (2,5), (3, 6) ] 
assert zip2([1,2,3,4,5],['a','b','c','d','e']) == [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')] 
assert zip2([2,4,6], ['fall','leaves']) == [(2, 'fall'), (4, 'leaves')]
assert zip2([], [4,5,6]) == []

