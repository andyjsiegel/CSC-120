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
        return self._data


def postorder(node):
    if node is None:
        return 
    postorder(node.left())
    postorder(node.right())
    print(node.value(), end=", ")

def inorder(node):
    if node is None:
        return 
    inorder(node.left())
    print(node.value(), end=",")
    inorder(node.right())

def sum_leaves(node):
    if node is None:
        return 0
    if node.left() == None and node.right() == None:
        return node.value()
    return sum_leaves(node.left()) + sum_leaves(node.right())
    

root = TreeNode(1)
nodeA = TreeNode(2)
nodeB = TreeNode(3)
nodeC = TreeNode(4)
nodeD = TreeNode(5)
nodeE = TreeNode(6)
nodeF = TreeNode(7)
nodeG = TreeNode(8)

root._left = nodeA
root._right = nodeB

nodeA._left = nodeC
nodeA._right = nodeD

nodeB._left = nodeE
nodeB._right = nodeF

nodeF._left = nodeG

# Traverse
# postorder(root)

root = TreeNode(1)
nodeA = TreeNode(2)
nodeB = TreeNode(3)
nodeC = TreeNode(4)
nodeD = TreeNode(5)
nodeE = TreeNode(6)
nodeF = TreeNode(7)
nodeG = TreeNode(8)

root._left = nodeA
root._right = nodeB

nodeA._left = nodeC
nodeA._right = nodeD

nodeB._left = nodeE
nodeB._right = nodeF

nodeF._left = nodeG

# Traverse
inorder(root)
print('\n')
print(sum_leaves(root))

