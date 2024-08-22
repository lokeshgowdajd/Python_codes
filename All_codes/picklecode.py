import pickle

class Employee:
    def __init__(self, name, age, salary, role):
        self.name = name
        self.age = age
        self.salary = salary
        self.role = role
    
    def __str__(self):
        return f"Employee(Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Role: {self.role})"

# Create an instance of Employee
e1 = Employee("Lokesh", 23, 20000, "QA")

# Serialize the object to a file
with open('employee.pkl', 'wb') as f:
    pickle.dump(e1, f)

print("Employee object serialized.")

# Deserialize the object from the file
with open('employee.pkl', 'rb') as f:
    e1_loaded = pickle.load(f)

print("Employee object deserialized.")
print(e1_loaded)
