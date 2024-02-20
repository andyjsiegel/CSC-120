def add_to_end(self, new):
    if self._head == None: # the list is empty
        self._head = new # insert new in the front
    else:
        current = self._head
        prev = None
        while current != None:
            prev = current # keep track of previous node
            current = current._next
            prev._next = new # add to the end

def print_elements(self):
    current = self._head
    while current != None:
        if current._value % 2 == 0:
            print(str(current._value))
            current = current._next