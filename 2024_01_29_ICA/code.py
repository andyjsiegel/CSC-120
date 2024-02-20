class Counter: 
    def __init__(self, name): 
        self._name = name
        self._count = 0 
    def click(self): 
        self._count -= -1
    def count(self): 
        return self._count 
    def __repr__(self):
        return f"name: {self._name}\ncount: {self._count}"
    def __str__(self): 
        return "Counter :" + self._name + "->" +  str(self._count)
    
import math 
class Point: 
    def __init__(self, x, y): 
        self._x = x  
        self._y = y 
    def __eq__(self, other):
        return self._x == other._x and self._y == other._y
    def translate(self, dx, dy): 
        self._x += dx 
        self._y += dy 
    def distance_from_origin(self): 
        return math.sqrt(self._x**2 + self._y**2) 

class Fraction():
    def __init__(self, n, d):
        self._num = n
        self._dem = d
    def __str__(self):
        return f"{self._num}/{self._dem}"
    def __eq__(self, other):
        return (self._num)/(self._dem) == (other._num)/(other._dem)
    def get_numerator(self):
        return self._num
    def get_denominator(self):
        return self._num
    
x = Fraction(1,2)
print(x) # '1/2' 
y = Fraction(4,8) # '4/8' 
print(y)

print(x == y) # True

counter = Counter('h')
counter.click()
counter.click()
print(counter)
