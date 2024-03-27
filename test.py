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

with open('gen_eds.txt') as f:
    data = f.read()
    classes = re.split('<!-- End HTML Area -->|<!-- Begin HTML Area Name Undisclosed -->', data)
    
    for class_data in classes:
        class_titles = re.findall(r'<span>(.*?)</span>', class_data)
        
        for class_title in class_titles:
            print(class_title)  # Display each class title
            
            # Extract instructor name, meeting location, and instruction mode for each class
            instructor_name = instructor_pattern.search(class_data).group(1) if instructor_pattern.search(class_data) else "Not Found"
            meeting_location = meeting_location_pattern.search(class_data).group(1) if meeting_location_pattern.search(class_data) else "Not Found"
            instruction_mode = instruction_mode_pattern.search(class_data).group(1) if instruction_mode_pattern.search(class_data) else "Not Found"
            
            print("Instructor's Name:", instructor_name)
            print("Meeting Location:", meeting_location)
            print("Instruction Mode:", instruction_mode)
            print("\n")
