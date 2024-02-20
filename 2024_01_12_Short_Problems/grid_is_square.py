def grid_is_square(arglist):
    for row in arglist:
        if len(row) != len(arglist):
            return False
    return True

print(grid_is_square([ [1,2,3], [4,5,6], [7,8,9]]))