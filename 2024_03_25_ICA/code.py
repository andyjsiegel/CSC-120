import math
# Write a program that reads a file and  computes (and prints out)
# the length of the longest line in that file. 
def get_longest_line(filename: str) -> int:
    list_ = []
    with open(filename) as file:
        for line in file:
            list_.append(len(line))

    print(max(list_))

get_longest_line('gen_eds.txt')


def my_sqrt(n: float) -> float: 
    assert n >= 0
    return math.sqrt(n)

def complex_sqrt(n: float) -> float:
    if n >= 0:
        return math.sqrt(n)
    else:
        return str(math.sqrt(abs(n))) + 'i'

print(complex_sqrt(4))
print(complex_sqrt(-4))

def has_evens(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
    return False
