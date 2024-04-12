def has_dups(alist):
    for num in alist:
        clone = list(alist)
        clone.pop(clone.index(num))
        for num2 in clone:
            if num == num2:
                return True
    return False

def has_dups2(alist):
    nums = {}
    for num in alist:
        if num in nums:
            return True
        nums[num] = '=D'
    return False

print(has_dups([1,2,3,4,5]))
print(has_dups([1,2,2,4,5]))
print(has_dups2([1,2,3,4,5]))
print(has_dups2([1,2,2,4,5]))