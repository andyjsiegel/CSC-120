def list2dict(list2d):
    the_dict = {}
    for sublist in list2d:
        the_dict[sublist[0]] = sublist[1:]
    return the_dict

fruits = [
    ['apple', 'banana', 'cherry', 'date'],
    ['elderberry', 'fig', 'grape', 'honeydew'],
    ['imbe', 'jackfruit', 'kiwi', 'lemon'],
    ['mango', 'nectarine', 'orange', 'pear']
]
print(list2dict(fruits))