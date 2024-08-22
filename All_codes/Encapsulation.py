class Person:
    def __init__(self, name, phonenumber):
        self.name = name  
        self.__phonenumber = phonenumber
    def get_phone(self):
        return self.__phonenumber



person = Person("Lokesh", 9117737227)

print(f"Name of the person: {person.name}")  

# Accessing private attribute via public methods
print(f"Phone number of the person: {person.get_phone()}")



