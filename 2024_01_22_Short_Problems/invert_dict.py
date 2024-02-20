def invert_dict(origdict):
    orig_values = (list(origdict.values()))
    orig_keys = (list(origdict.keys()))
    new_dict = {}
    for i in range(len(orig_values)):
        new_dict[orig_values[i]] = orig_keys[i]
    return new_dict

print(invert_dict({'a': 1, 'b': 2, 'c': 3}))