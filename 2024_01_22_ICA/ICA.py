def identify_unique_words(slist):
    the_dict = {}
    for word in slist:
        if word in the_dict:
            the_dict[word] = 1
        else:
            the_dict[word] = 0
    print(the_dict)
    return the_dict

def find_courses(catalog, units):
    courses = []
    # units = 3
    # catalog = {'MIS': { 'mis 102':3 }, 'CSC': {'csc 110': 3} }
    for dept in catalog.values():
        for key, value in dept.items():
            if value == units:
                courses.append(key) 
    print(courses)
    return courses

find_courses({'MIS': { 'mis 102':3 }, 'CSC': {'csc 110': 3} }, 3)

    