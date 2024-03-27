class TreeNode:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None
    def left(self):
        return self._left
    def right(self):
        return self._right
    def value(self):
        return str(self._data)
    def is_leaf(self):
        if self._left == None and self._right == None:
            return 'L'
        return ''

def inorder(node):
    if node is None:
        return 
    inorder(node.left())
    print(node.value())
    inorder(node.right())

def notate_leaves(bt):
    if bt is None:
        return 
    notate_leaves(bt.left())
    is_leaf = bt.is_leaf()
    print(str(bt.value()) + is_leaf)
    notate_leaves(bt.right())

root = TreeNode(3)
nodeA = TreeNode(9)
nodeB = TreeNode(7)
nodeC = TreeNode(2)
nodeD = TreeNode(8)
nodeE = TreeNode(24)

root._left = nodeA
root._right = nodeB

nodeA._left = nodeC
nodeA._right = nodeD

nodeB._left = nodeE


# Traverse
notate_leaves(root)

class BinaryTree: 
    def __init__(self,value): 
        self._value = value 
        self._left = None 
        self._right = None 
    def value(self): 
        return self._value 
    def left(self): 
        return self._left 
    def right(self): 
        return self._right
    
    def insert_right(self, value):
        if self._right is None:
            self._right = value
        else:
            value._right = self._right
            self._right = value

    def insert_left(self, value):
        if self._left is None:
            self._left = value
        else:
            value._left = self._left
            self._left = value

the_tree = BinaryTree(6)
the_tree.insert_left(BinaryTree(15))
the_tree.insert_right(BinaryTree(2))
the_tree.right().insert_right(BinaryTree(8))