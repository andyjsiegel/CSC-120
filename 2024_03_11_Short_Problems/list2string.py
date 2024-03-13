def list2string(arglist):
    if arglist == []:
        return ""
    return str(arglist[0]) + list2string(arglist[1:])

print(list2string(["h","e","l","l","o"]))