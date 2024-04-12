def words_ending_with(wordlist, tail): 
    outlist = [] 
    for item in wordlist: 
        if item.endswith(tail): 
            outlist.append(item) 
    return outlist 


wordlist, tail = ["apple", "banana", "orange"], "e"
assert words_ending_with(wordlist, tail) == ["apple", "orange"]

wordlist, tail = [], "ing"
assert words_ending_with(wordlist, tail) == []

wordlist, tail = ["jumping", "running", "swimming"], "ing"
assert words_ending_with(wordlist, tail) == ["jumping", "running", "swimming"]

wordlist, tail = ["Hello", "world", "endIng"], "Ing"
assert words_ending_with(wordlist, tail) == ["endIng"]

def my_function(lst): 
    if len(lst)>5: 
        print('ifblock ran')
        for i in range(5): 
            if lst[i]<lst[i+1]: 
                print("{}-th element is smaller than {}-th element".format(i, i+1)) 
    else: 
        print('elseblock ran')
        for i in range(len(lst)-1): 
            if lst[i]<lst[i+1]: 
                    print("{}-th element is smaller than {}-th element".format(i, i+1)) 

# # if block
# my_function([1,2,3,4,5,6,7,8,9,10])
# my_function([6,3,7,9,15,4])
# # else block
# my_function([1,2,3,4])
# my_function([2,4,6,8])
def move_max_to_end(lst): 
    for i in range(len(lst)-1): 
        if lst[i]>lst[i+1]: 
            t = lst[i] 
            lst[i] = lst[i+1] 
            lst[i+1] = t 

# assert move_max_to_end([69,1,4,2,3,8])[-1] 
llist = [69,1,4,2,3,8]
move_max_to_end(llist)
assert llist[-1] == max(llist)