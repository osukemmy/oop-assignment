# polymorphism.py
# Activity 2: Polymorphism Challenge

class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is running 🐕"

class Fish(Animal):
    def __init__(self, species):
        self.species = species

    def move(self):
        return f"The {self.species} is swimming 🐟"

class Bird(Animal):
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is flying 🐦"

# Vehicle hierarchy
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Car(Vehicle):
    def __init__(self, model):
        self.model = model

    def move(self):
        return f"{self.model} is driving 🚗"

class Plane(Vehicle):
    def __init__(self, model):
        self.model = model

    def move(self):
        return f"{self.model} is flying ✈️"

# Demonstration function showing polymorphism
def demonstrate():
    things = [
        Dog("Rover"),
        Fish("goldfish"),
        Bird("Tweety"),
        Car("Toyota Corolla"),
        Plane("Boeing 737"),
    ]

    for obj in things:
        # We simply call the same method name on different objects
        print(obj.move())

if __name__ == "__main__":
    demonstrate()
