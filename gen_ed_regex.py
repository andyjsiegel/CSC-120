import re

# Define a custom sorting key function
def extract_class_number(title):
    # Extract the numeric part of the class title
    match = re.search(r'(\d+)', title)
    if match:
        class_number = match.group(1)
    else:
        class_number = title

    return int(class_number)

# Regex patterns for extracting information
instructor_pattern = re.compile(r'Instructor</span><div>(.*?)</div>')
meeting_location_pattern = re.compile(r'Meeting Location</span><div>(.*?)</div>')
instruction_mode_pattern = re.compile(r'Instruction Mode</dt><dd>(.*?)</dd>')

classes_data = []

with open('gen_eds2.txt') as f:
    data = f.read()
    classes = data.split('<div class="card mb-4 ng-star-inserted">')[1:]

    for class_data in classes:
        class_titles = re.findall(r'<span>(.*?)</span>', class_data)
        
        for class_title in class_titles:
            print(' '.join(class_title.split()))

                    
            # Extract instructor name, meeting location, and instruction mode for each class title
            instructor_match = instructor_pattern.search(class_data)
            instructor_name = instructor_match.group(1) if instructor_match else "Not Found"
            
            location_match = meeting_location_pattern.search(class_data)
            meeting_location = location_match.group(1) if location_match else "Not Found"
            
            mode_match = instruction_mode_pattern.search(class_data)
            instruction_mode = mode_match.group(1) if mode_match else "Not Found"
            
            # print("   Instructor's Name:", instructor_name)
            # print("   Meeting Location:", meeting_location)
            # print("   Instruction Mode:", instruction_mode)
            # print(" ")

