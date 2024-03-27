class BinaryTree: 
    def __init__(self,value): 
        self._value = value 
        self._left = None 
        self._right = None 
    def value(self, *value): 
        if value:
            self._value = value[0]
        return self._value 
    def left(self, *left): 
        if left:
            if type(l := left[0]) != BinaryTree:
                self._left = BinaryTree(l)
            else:
                self._left = l
        return self._left 
    def right(self, *right): 
        if right:
            if type(r := right[0]) != BinaryTree:
                self._right = BinaryTree(r)
            else:
                self._right = r
                
        return self._right 
    def __str__(self, level=0):
        ret = "\t" * level + repr(self._value) + "\n"
        if self._left:
            ret += self._left.__str__(level + 1)
        if self._right:
            ret += self._right.__str__(level + 1)
        return ret

def breadth_first(tree):
    if tree is None:
        return
    
    q = [tree]
    while len(q) > 0:

        print(q[0].value())
        node = q.pop(0)

        if (l := node.left()) is not None:
            q.append(l)

        # Enqueue right child
        if (r := node.right()) is not None:
            q.append(r)


root = BinaryTree(1)
root._left = BinaryTree(2)
root._right = BinaryTree(3)
root._left._left = BinaryTree(4)
root._left._right = BinaryTree(5)

# print("Level Order Traversal of binary ree is -")
# breadth_first(root)
# print('\n\npreorder:')

def print_preorder(node):
    if node is None:
        return 
    
    print(node.value())
    print_preorder(node.left())
    print_preorder(node.right())

def print_inorder(node):
    if node is None:
        return
    print_inorder(node.left())
    print(node.value())
    print_inorder(node.right())


# print_preorder(root)

def preorder_list(tree):
    preorder = []
    if tree is None:
        return []
    
    preorder += [tree.value()]
    preorder += preorder_list(tree.left())
    preorder += preorder_list(tree.right())
    return preorder
    

# print(preorder_list(root))

BST = BinaryTree(12)
BST.left(5)
rll = BST.right(80).left(76).left(62)
rll.left(30)
rll.right(68)
BST.right().right(85)
print(BST)

# print_preorder(BST)
print_inorder(BST)
