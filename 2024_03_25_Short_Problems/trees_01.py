class BinarySearchTree:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def add(self, val):
        if self.value is None:
            self.value = val
        elif val < self.value:
            if self.left is None:
                self.left = BinarySearchTree()
            self.left.add(val)
        else:
            if self.right is None:
                self.right = BinarySearchTree()
            self.right.add(val)

    def find(self, val):
        if self.value == val:
            return self
        elif val < self.value and self.left:
            return self.left.find(val)
        elif val > self.value and self.right:
            return self.right.find(val)
        else:
            return None

    def __str__(self):
        if self is None:
            return "None"
        else:
            return "({:d} {} {})".format(self.value, str(self.left), str(self.right))