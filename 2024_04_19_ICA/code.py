def log10(val):  
    count = 0
    while val > 1:
        val = val / 10
        count += 1
    return count

assert log10(10) == 1
assert log10(18) == 2
assert log10(100) == 2
assert log10(108) == 3
assert log10(1000) == 3
assert log10(1008) == 4

def is_BST(root):
    if root is None:
        return True
    if root._left is None and root._right is None:
        return True
    if (root._left is not None and root._left._val > root._val) or (root._right is not None and root._right._val < root._val):
        return False
    return is_BST(root._left) and is_BST(root._right)

 
