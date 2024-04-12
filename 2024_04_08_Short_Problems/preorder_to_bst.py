class BinarySearchTree:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    def __str__(self):
        if self == None:
            return 'None'
        else:
            return "({:d} {} {})".format(self._value
                , str(self._left), str(self._right))

def preorder_to_bst(preorder):
    if len(preorder) == 0:
        return None
    else:
        root = BinarySearchTree(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < preorder[0]:
            i += 1
        root._left = preorder_to_bst(preorder[1:i])
        root._right = preorder_to_bst(preorder[i:])
        return root

