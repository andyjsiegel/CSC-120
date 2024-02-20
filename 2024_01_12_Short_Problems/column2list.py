def column2list(grid, n):
   column = []
   for row in grid:
        column.append(row[n])
   return column

grid = [ [1,2,3], [4,5,6], [7,8,9] ]
print(column2list(grid, 2))
grid2 = [ [ 'aa', 'bb', 'cc', 'dd' ], [ 'ee', 'ff', 'gg', 'hh', 'ii', 'jj' ], [ 'kk', 'll', 'mm', 'nn' ] ]
print(column2list(grid2, 3))