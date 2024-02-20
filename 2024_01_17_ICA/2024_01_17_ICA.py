# for i in range(100,0,-2):
#     print(i)

# the_list = [1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(the_list),2):
#     print(the_list[i])

# def get_words(str):
#     list = str.split('-')
#     return list

# def sum_column(grid, offset):
#     the_list = []
#     for sub_list in grid:
#         the_list.append(int(sub_list[offset]))
#     return sum(the_list)

# print(sum_column([['h', 'j', '1', 'x'], ['m', 'p', '4', 'c'], ['c', 'a', '3', 'r'], ['j', 'z', '2', 'b']], 2))

def print_some_words(file_name, n):
    f = open(file_name, 'r')
    for line in f.readlines():
        for word in line.split(' '):
            if len(word) >= n:
                print(word.strip('.,;\n'))

print_some_words('poem.txt', 6)