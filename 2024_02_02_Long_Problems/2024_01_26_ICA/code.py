class Counter: 
    def __init__(self, name): 
        self._name = name 
        self._count = 0 
        self._reset_count = 0
    def click(self): 
        self._count += 1 
    def count(self): 
        return self._count
    def reset(self):
        self._count = 0
        self._reset_count += 1
    def __str__(self):
	    return f"Name: {self._name}\nCount: {self._count}\nReset Count: {self._reset_count}"

counter = Counter("andy")
counter.click()
counter.count()
counter.click()
counter.count()
print(counter.__str__())
counter.reset()
print(counter.__str__())