class Employee:
    def __init__(self, name, age, salary, role):
        self.name = name
        self.age = age
        self.salary = salary
        self.role = role
E1 = Employee("Lokesh", 23, 20000, "QA")

print(E1.name)
print(E1.age)
print(E1.salary)
print(E1.role)