class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animals = [Dog(), Cat(), Animal()]
for a in animals:
    a.speak()


# Partial Override
class Employee:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Employee: {self.name}"

class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size

    def describe(self):
        base = super().describe()
        return f"{base}, manages {self.team_size} people"


# 1 Create a Shape class with an info() method that returns "I am a shape". 
# Create Circle and Square children that override info() with their own messages.
class Shape:
    def info(self):
        return "I am a Shape"

class Circle(Shape):
    def info(self):
        return "I am a Circle"

class Square(Shape):
    def info(self):
        return "I am a Square"        
 

# 2 Create a Vehicle class with a fuel_type() method returning "Unknown".
#  Override it in ElectricCar to return "Electric" and in GasCar to return "Gasoline".
class Vehicle:
    def fuel_type(self):
        return "Unknown"
class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric"   
class GasCar(Vehicle):
    def fuel_type(self):
        return "Gasoline"   
# 3 Create a Person class with a greet() method. 
# Create a FormalPerson that does a partial override, calling super().greet() and adding "Pleased to meet you."
class Person:
    def greet(self):
        return "Hello , I am Person class"    
class FormalPerson(Person):
    def greet(self):
        greet = super().greet()
        return greet + "Please to meet you"
        
            