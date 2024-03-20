class Node:
    pass

def insert(T, v):
    if T == None:
        return Node(v)
    
    if v < T.value:
        T.left = insert(T.left, v)
    elif v > T.value:
        T.right = insert(T.right, v)
    
    return T