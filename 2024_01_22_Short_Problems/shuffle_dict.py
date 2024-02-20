def shuffle_dict(somedict):
    sorted_keys = sorted(list(somedict.keys()))
    sorted_vals = sorted(list(somedict.values()))
    new_dict = {}
    for i in range(len(sorted_keys)):
        new_dict[sorted_keys[i]] = sorted_vals[i]
    return new_dict

my_dict = {'banana': 3, 'apple': 1, 'orange': 2}
print(shuffle_dict(my_dict))