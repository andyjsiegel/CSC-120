def count_odds(alist):
    if not alist:
        return 0
    if alist[0] % 2 != 0:
        return 1 + count_odds(alist[1:])
    return count_odds(alist[1:])
