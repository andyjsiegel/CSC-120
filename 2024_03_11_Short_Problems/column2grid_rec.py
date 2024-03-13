def column2list_rec(grid, n):
    if grid == []:
        return []
    else:
        return [grid[0][n]] + column2list_rec(grid[1:], n)
    
print(column2list_rec([ [ 'aa', 'bb', 'cc', 'dd' ],[ 'ee', 'ff', 'gg', 'hh', 'ii'],[ 'kk', 'll', 'mm', 'nn' ] ], 3))