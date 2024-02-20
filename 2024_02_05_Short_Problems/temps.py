class Temp:
    def __init__(self, temp, unit):
        self._temp = temp
        self._unit = unit
    
    def normalize_temp(self):
        if self._unit == 'C':
            return self._temp
        else:
            return (self._temp - 32) * 5/9
    
    def __str__(self):
        return str(self._temp) + self._unit
    
    def __eq__(self, other):
        return self.normalize_temp() == other.normalize_temp()
