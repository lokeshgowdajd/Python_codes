from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, breed):
        self.name = name
        self.breed=breed

    @abstractmethod
    def sound(self):
        pass
   
class Dog(Animal):
    def sound(self):
        return "Boww!!"

class Cat(Animal):
    def sound(self):
        return "Meoww!!"


dog = Dog("Sufhy","pomorian")
cat = Cat("lite", "persian")


print(f"{dog.name} makes the sound: {dog.sound()}") 
print(f"{cat.name} makes the sound: {cat.sound()}") 
