def sum_odds(alist):
    if not alist:
        return 0
    if alist[0] % 2 != 0:
        return alist[0] + sum_odds(alist[1:])
    return sum_odds(alist[1:])
