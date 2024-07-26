import re

pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

# Read file contents
with open('Python.txt', 'r') as file:
    file_contents = file.read()

# Split file contents into lines
lines = file_contents.splitlines()

# Process each line
for line in lines:
    line = line.strip() 
    match = pattern.search(line)
    
    if match:
        print(f"Matched: {match.group()}")
    
        
