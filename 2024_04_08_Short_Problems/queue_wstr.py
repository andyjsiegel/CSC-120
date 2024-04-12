class Queue:
    def __init__(self):
        self.items = ""

    def enqueue(self, item):
        self.items += item

    def dequeue(self):
        dequeued_item = self.items[0]
        self.items = self.items[1:]
        return dequeued_item

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return self.items