class Animal:
    def __init__(self, name):
        self.name = name

    def speek(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(f"Animal name is {animal.name}: {animal.speak()}")

dog = Dog("Pomorian")
cat = Cat("Persian")

make_animal_speak(dog)  
make_animal_speak(cat)  
