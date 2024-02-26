str = "The Doctor (David Tennant) (Doctor Who)	29	0"
values = str.split()
conf = []
boolean = False
index_of_name = 0
for val in values[::-1]:
    print(val)
    if ')' in val:
        boolean = True
    if boolean:
            conf.append(val)
    if '(' in val:
         boolean = False
         index_of_name = values.index(val)
         break
    
print('Conference:')
print(' '.join(conf[::-1]).strip('()'))
print('Team name:')
print(' '.join(values[0:index_of_name]))