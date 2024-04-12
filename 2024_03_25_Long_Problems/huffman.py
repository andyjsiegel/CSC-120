"""
File: huffman.py
Author: Andy Siegel
Course: CSC 120, Spring 2024
Purpose: This program implements a BinaryTree class to decode a sequence of 0s
    and 1s. The program takes in a preorder sequence, inorder sequence, and 
    encoded sequence. It constructs a binary tree with the preorder and 
    inorder sequences, then prints the postorder sequence of the binary tree
    and then prints the decoded sequence. 
    """

class BinaryTree: 
    """
    This class represents a binary tree. It has value, left, and right
    attributes. It has 3 getters for left, right, and value along with an 
    is_leaf() function which returns True if the left and right subtrees are 
    None. Otherwise, it returns False.
    """
    def __init__(self,value): 
        """
        This method initializes the binary tree class by taking in a value and 
        settings the corresponding attribute to it, then giving the left and 
        right subtrees a default value of None.
        """
        self._value = value 
        self._left = None 
        self._right = None 

    def value(self): 
        return self._value
    
    def left(self): 
        return self._left 
    
    def right(self): 
        return self._right
    
    def is_leaf(self):
        """
        This function checks whether the current node is a leaf node by
        checking if it has any child nodes. If it does not have any child
        nodes, it returns True, otherwise it returns False.
        Parameters:
            None
        Returns:
            a boolean according to whether the node is a leaf node.
        """
        if self._left == None and self._right == None:
            return True
        return False
    
    def __str__(self):
        return f'[{self._value}, {self._left}, {self._right}]'
   
def construct_tree(preorder_seq, inorder_seq):
    """
    This function takes in two sequences, a preorder sequence and an inorder 
    sequence, and constructs a binary tree using those sequences. It 
    recursivelycalls itself to construct the left and right subtrees, using the 
    first value in the preorder sequence as the root and finding its index in 
    the inorder sequence.
    Args:
        preorder_seq
        inorder_seq
    Returns:
        root: the created binary tree
    """
    # to make tree, both seqs must be defined.
    if not preorder_seq or not inorder_seq:
        return None

    # first value of a preorder seq is the root.
    root_value = preorder_seq[0]
    root = BinaryTree(root_value)

    root_index = inorder_seq.index(root_value)

    # preorder_seq[1:1 + root_index] is sublist of all elements in the left 
    # subtree as is inorder_seq[:root_index]

    root._left = construct_tree(preorder_seq[1:1 + root_index],\
        inorder_seq[:root_index])
    root._right = construct_tree(preorder_seq[1 + root_index:],\
        inorder_seq[root_index + 1:])

    return root

def decode_seq(tree, encoded_seq):
    """
    This function takes in a binary tree and an encoded sequence and decodes 
    the sequence by traversing the tree based on the bits in the sequence 
    (huffman coding). It returns the decoded sequence as a string.
    Args:
        tree
        encoded_seq
    Returns:
        decoded_seq
    """
    decoded_seq = ""
    current_node = tree
    for bit in encoded_seq:
        if bit == 0:
            current_node = current_node.left()
        elif bit == 1:
            current_node = current_node.right()
        
        if current_node != None:
            if current_node.is_leaf():
                decoded_seq += current_node.value()
                current_node = tree

    return decoded_seq

def postorder(node):
    """
    This function performs a postorder traversal of a binary tree, printing out
    the values of each node in the order of left child, right child, and then 
    the current node. If the node is empty, it returns nothing.
    Args:
        node
    Returns:
        None
    """
    if node is None:
        return
    postorder(node.left())
    postorder(node.right())
    print(node.value(), end=" ")

def handle_file(filename):
    """
    This function takes in a filename and uses the information in the file to 
    construct a binary tree and decode a sequence using that tree.
    Args:
        filename
    Returns:
        None
    """
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    preorder, inorder, encoded_seq = lines[0], lines[1], lines[2]
    # use .split() to pass in lists of integers rather than strings
    tree = construct_tree(preorder.split(), inorder.split())
    
    # convert encoded_seq string to a list of integers
    encoded_seq_list = []
    for char in encoded_seq.strip():
        encoded_seq_list.append(int(char))

    # print postorder, then print the decoded sequence
    postorder(tree)
    print('\n' + decode_seq(tree, encoded_seq_list))

def main():
    file = input('Input file: ')
    handle_file(file)
   
if __name__ == '__main__':
    main()
