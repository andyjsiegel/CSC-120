# 1 last 2 chars
text = input()
if len(text) < 2:
    print('')
else:
    print(text[-2:])

# 2 count occurences
text = "To be or not to be, that is the question."
letter = 'o'
count = 0
c = 0
while c < len(text):
    if text[c] == letter:
        count += 1
    c += 1

# 3 list syntax
x = [ 'abc', 'def', 'ghi', 'jkl' ] 
x[1] + x[-1] # abcjkl

# 4 get evens
num = [18, 3, 24, 63, 18, 4, 7]
i = 0
evens = []
while i < len(num):
    if num[i] % 2 == 0:
        evens.append(num[i])
    i+= 1

# 5 get element in 2d list
y = [['aa', 'bb', 'cc'], ['dd', 'ee', 'ff'], ['hh', 'ii', 'jj']]
y[0][1] # bb
    
# 6 sum first column (while): 
x = [ [1,2,3], [10,20,30], [100,200, 300]]
sum, i = 0, 0
while i < len(x):
	sum += x[i][0]
	i+= 1

# 7 sum first column (for in range)
x = [ [1,2,3], [10,20,30], [100,200, 300]]
sum = 0  
for i in range(len(x)):
    sum += x[i][0]

# 8 sum first column (for in range)
x = [ [1,2,3], [10,20,30], [100,200, 300]]
sum = 0  
for row in x:
    sum += row[0]

# 9 turn sentence into list and remove punctuation