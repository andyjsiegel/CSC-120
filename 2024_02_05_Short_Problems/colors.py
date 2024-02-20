class Color:
    def __init__(self, r, g, b):
        self._r = r
        self._g = g
        self._b = b
    def fix_values(self):
        if self._r < 0:
            self._r = 0 
        if self._r > 255:
            self._r = 255 
        if self._g < 0:
            self._g = 0 
        if self._g > 255:
            self._g = 255 
            
        if self._b < 0:
            self._b = 0 
        if self._b > 255:
            self._b = 255 
    def remove_red(self):
        self._r = 0
    def __eq__(self, other):
        return self.get_rgb() == other.get_rgb()
    def __str__(self):
        return f'Color({self._r},{self._g},{self._b})'
    def get_rgb(self):
        return (self._r, self._g, self._b)
    
color1 = Color(135,50,140)
color1.remove_red()
print(color1)