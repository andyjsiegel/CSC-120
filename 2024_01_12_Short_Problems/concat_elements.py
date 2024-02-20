def concat_elements(slist, startpos, stoppos):
    if startpos > stoppos:
        return ""
    if startpos < 0:
        startpos = 0
    if stoppos > len(slist)-1:
        stoppos = len(slist)-1
    str = ""
    for i in range(startpos, stoppos+1):
        str += slist[i]
    return str

# slist = ['apple','banana','orange','pineapple']
# startpos = 1
# stoppos = 2
# print(concat_elements(slist, startpos, stoppos))