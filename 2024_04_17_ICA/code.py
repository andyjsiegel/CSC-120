def hash(key, table_size): 
    return sum([ord(char)*(index+1) for index, char in enumerate(key)]) % table_size

print(hash("banana",5))

# import Random 
# a = random.randint(1,12) 
# b = random.randint(1,12) 
# for i in range(l0): 
#     question = "What is "+a+" x "+b+"? " 
#     answer = input(question) 
#     if answer = a*b  
#         print (Well done!) 
#     else: 
#         print("No.") 

# def remove_dupes(alist): 
#     count = len(alist) 
#     i = 0  
#     while i < count: 
#         j = i  
#         while j < count:
#             try:
#                 if alist[j] == alist[i]: 
#                     alist.pop(j) 
#             except:
#                 continue
#             j += 1

#         i += 1

# print(remove_dupes([-50, 66, 80, 58, -50, 86, -19, -35, 45, 80, 80, -6, 34]))

def sort_input(): 
    data = [] 
    while True: 
        val = input("Enter a number (blank line to end) ")
        if val == "":  
            break 
        data.append(val) 
    for v in sorted(data): 
        print(v)

sort_input()
