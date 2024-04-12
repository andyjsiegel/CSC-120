def remove_last(self):
    if self._head is None:
        return None
    if self._head == self._tail:
        val = self._head
        self._head = None
        self._tail = None
        return val
    current = self._head
    while current._next != self._tail:
        current = current._next
    val = self._tail
    current._next = None
    self._tail = current
    return val