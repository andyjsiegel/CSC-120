class EveryOther:
    def __init__(self, data):
        self._data = data
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration
        result = self._data[self._index]
        self._index += 2
        return result

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
every_other_iterator = EveryOther(data)

# for element in every_other_iterator:
#     print(element)

# def every_other(data):
#     index = 0
#     while index < len(data):
#         yield data[index]
#         index += 2

# result = every_other(data)

def get_min(invent_dict):
    return [(key, value) for key, value in invent_dict.items() if value == min(invent_dict.values())]

# Example usage
d = {"spoons": 7, "knives": 8, "forks": 6, "plates": 10}
result = get_min(d)
print(result)



