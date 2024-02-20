def concat_elements2(slist, startpos, stoppos):
    if startpos > stoppos:
        return ""
    if startpos < 0:
        startpos = 0
    if stoppos > len(slist)-1:
        stoppos = len(slist)-1
    return ''.join(slist[startpos:stoppos+1])