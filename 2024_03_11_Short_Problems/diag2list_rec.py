def slice_each_inner_list(a_2d_list, pos):
    if a_2d_list == []:
        return []
    return [a_2d_list[0][pos]] + slice_each_inner_list(a_2d_list[1:], pos+1)

def diag2list_rec(grid):
    return slice_each_inner_list(grid, 0)
    

    
print(diag2list_rec([ [ 'aa', 'bb', 'cc' ],[ 'ee', 'ff', 'gg'],[ 'kk', 'll', 'mm'] ]))
# assert diag2list_rec([ [ 'aa', 'bb', 'cc' ],[ 'ee', 'ff', 'gg'],[ 'kk', 'll', 'mm'] ]) == ['aa', 'ff', 'mm']