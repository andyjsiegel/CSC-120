catalog = { 'MIS': {'mis 101': 4, 'mis 102': 3, 'mis 202': 2},
 'CSC': {'csc 110': 4, 'csc 120': 4, 'csc 352': 3},
 'ECE': {'ece 111': 3, 'ece 222': 3, 'ece 333': 4}}

def add_course_to_catalog(course_to_add, units):
    dept = course_to_add.split(' ')[0].upper()
    if dept not in catalog:
        catalog[dept] = {}
    catalog[dept][course_to_add] = units
    return catalog

# add_course_to_catalog("ece 444", 4)
# add_course_to_catalog("math 223", 3)        
    
def num_keys(two_level_dict):
    keys = []
    for key in two_level_dict:
        keys.append(key)
        for second_key in two_level_dict[key]:
            keys.append(second_key)
    return len(keys)

# mydict = { 12 : { 'a' : 11, 'b': 22},
#  23 : { 'm' : 33, 'b': 44, '5': 55 } }
# print(num_keys(mydict))

def max_min(L):
    evens = []
    for num in L:
        if num % 2 == 0:
            evens.append(num)
    return (min(evens), max(evens))

# lsit = [1,2,3,4,5,6,7]
# print(max_min(lsit))

def print_k_v(the_dict):
    for k,v in sorted(the_dict.items()):
        print(f"{k}:{v}")

print_k_v(catalog)

v = "ABCDEFGHIJ"
w = ( ('aa','ab','bc'), (12, 23, 34), [45, 56, 67, 78] )
x = { 'abc' : 12, 'cde' : 34, 'efg' : 56 }
y = [ ['pqr', 'stu','abc','def'], ['uvw','xyz','bcd','cde'] ]

w[2][3] = 'hello'

