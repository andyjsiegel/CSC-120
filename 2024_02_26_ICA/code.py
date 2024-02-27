class Queue: 
    def __init__(self): 
        self._items = []
    def enqueue(self, item): 
        self._items.append(item)
    def dequeue(self):
        if self._items:  # Check if queue is not empty before dequeueing
            self._items.pop(0)

def hot_potato(q: Queue, num):
    for i in range(num):
        x = q.dequeue()
        q.enqueue(x)
    
    return q.dequeue()

def sumlist(alist):
    if not alist:
        return 0
    return alist[0] + sumlist(alist[1:])

def string_len(s):
    if not s:
        return 0
    return 1 + string_len(s[1:])

def join_all(alist, sep):
    if not alist:
        return ""
    if len(alist) == 1:
        return alist[0]
    return alist[0] + sep + join_all(alist[1:], sep)


print(join_all(['h','e','l','l','o'], '-'))

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

print(factorial(4))