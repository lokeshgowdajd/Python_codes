with open("Python.txt") as fh:
    
    count = sum(1 for line in fh for character in line if character.isupper())
print(f"Total uppercase letters in the file: {count}")