def str2objects(spec):
    conversion = {
        "str" : "",
        "dict" : {},
        "list" : []
    }
    objects = spec.split(None, 1)
    if len(objects) == 0:
        return []
    if len(objects) == 1:
        return [conversion[objects[0]]]
    else:
        return [conversion[objects[0]]] + str2objects(objects[1])

print(str2objects("dict list str dict")) # [{}, [], '', {}]