def update_dict2(dict2, key1, key2, value):
    if key1 not in dict2:
        dict2[key1] = {}
    dict2[key1][key2] = value
    return dict2
