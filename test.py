substring = '~`_~'
# substring = 'andy'
indices = [
    (2,4),
    (0,2),
    (1,2),
    (0,1),
    (0,2),
    (0,1),
    (0,2),
    (1,2),
    (0,1),
    (0,2),
    (1,2),
    (2,4),
    (0,2),
    (1,2),
    (0,1),
    (0,4),
    (0,2),
    (1,2),
    (3,4),
    (0,2),
    (1,4),
    (0,2),
    (1,2),
    (0,1),
    (0,1),
    (1,2),
    (1,2)
]
for index_pair in indices:
    print(substring[index_pair[0]:index_pair[1]], end="")

