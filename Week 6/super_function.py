class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # call parent's __init__
        self.student_id = student_id

s = Student("Alice", 20, "S001")
print(s.name)        # Alice -- set by parent
print(s.student_id)  # S001 -- set by child


# inside normal method 
class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def describe(self):
        return f"I am {self.name}"

class Dog(Animal):
    def describe(self):
        base = super().describe()
        return f"{base} and I am a {self.breed}"

d = Dog("Buddy", "Labrador")
print(d.describe())

# 1. Create a Product class with name and price.
# Create an Electronics child that adds warranty_years using super().
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Electronics(Product):
    def __init__(self, name, price,warranty_years):
        super().__init__(name, price) 
        self.warranty_years=warranty_years
prd=Electronics('Book',230,2)               

# 2. Create a Bird class with a describe() method. 
# Create a Parrot child that uses super().describe() and adds "and I can talk!".
class Bird:
    def describe(self):
        return "I am a Bird"
class Parrot(Bird):
    def describe(self):
        return super().describe()  +  " and I can talk"
p=Parrot()    
print(p)
# 3 Create a Account class with a display() method. 
# Create a SavingsAccount that extends display() using super() to also show the interest rate.
class Acount:
    def display(self):
        return "Display"
class SavingsAccount(Acount):
    def display(self):
        return super().display() + "Interest rate 12 %"