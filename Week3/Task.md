# Q1 In your own words, explain the difference between procedural and object-oriented programming.
## Procedural Programming follows step by step instructions.Its fouses on actions.Here, we write function that operate on data. Whereas object oriented programming organized code around objects that bundle data and behavior together.It focuses on things


# Q2 Name three real-world objects and list two attributes and two behaviors for each.
## The 3 real world objects are :- 
Object: Car

Attributes: color, make, model, year
Behaviors: start_engine(), accelerate(), brake(), turn()
Object: Smartphone

Attributes: brand, model, operating_system, screen_size
Behaviors: make_call(), send_text(), take_photo(), browse_internet()
Object: Dog

Attributes: breed, age, name, color
Behaviors: bark(), eat(), sleep(), fetch()

# Q3 Take the procedural student example above and add a third student. Then think about how the OOP version would handle it.
# Procedural Student Example
ankit_student1_name = "Alice"
ankit_student1_age = 18
ankit_student1_grade = "A"

ankit_student2_name = "Bob"
ankit_student2_age = 19
ankit_student2_grade = "B"

# Adding a third student procedurally
```
ankit_student3_name = "Charlie"
ankit_student3_age = 17
ankit_student3_grade = "A-"

print("Procedural Student Data:")
print(f"Student 1: {ankit_student1_name}, Age: {ankit_student1_age}, Grade: {ankit_student1_grade}")
print(f"Student 2: {ankit_student2_name}, Age: {ankit_student2_age}, Grade: {ankit_student2_grade}")
print(f"Student 3: {ankit_student3_name}, Age: {ankit_student3_age}, Grade: {ankit_student3_grade}")
```
## How OOP would handle it:
  -  In an OOP approach, we would define a 'Student' class with attributes like name, age, and grade.

  - Each student would be an 'object' (instance) of this class. Adding a new student means creating a new instance.

  - This makes the code cleaner, more organized, and easier to scale as the number of students or attributes grows.
```
class AnkitStudent:
    def __init__(self, name, age, grade):
        self.ankit_name = name
        self.ankit_age = age
        self.ankit_grade = grade

    def ankit_get_info(self):
        return f"Name: {self.ankit_name}, Age: {self.ankit_age}, Grade: {self.ankit_grade}"

print("\nOOP Student Data:")
ankit_student_obj1 = AnkitStudent("Alice", 18, "A")
ankit_student_obj2 = AnkitStudent("Bob", 19, "B")
ankit_student_obj3 = AnkitStudent("Charlie", 17, "A-") 
print(f"Student 1: {ankit_student_obj1.ankit_get_info()}")
print(f"Student 2: {ankit_student_obj2.ankit_get_info()}")
print(f"Student 3: {ankit_student_obj3.ankit_get_info()}")
```
# Create a class called Book with attributes title, author, and pages.
```
class Book:
     def __init__(self,title,author,pages):
         self.ankit_title=title
         self.ankit_author=author
         self.ankit_pages=pages
    def ankit_get_info(self):
         return f"The author of Book {self.ankit_title} is {self.ankit_author} which has {self.ankit_pages} pages"
```

# Create a class called Movie with attributes for title, director, and year.
```
class Movie:
     def __init__(self,title,director,year):
         self.ankit_title=title
         self.ankit_director=director
         self.ankit_year=year
    def ankit_get_info(self):
         return f"The director of Movie {self.ankit_title} is {self.ankit_director} which was released on {self.ankit_year} year"
```
# Create a class called PhoneContact with attributes for name, phone number, and email. Print each attribute.

```
class PhoneContact:
     def __init__(self,name,number,email):
         self.ankit_name=name
         self.ankit_author=number
         self.ankit_email
    def ankit_get_info(self):
         return f"The number of {self.ankit_name} is {self.ankit_number} whose email is {self.ankit_email}."
```

# Create a Fruit class with a name attribute. Create three fruit objects and give each a different name.
```
class Fruit:
    def __init__(self,name):
        self.ankit_name=name
    def ankit_get_fruit(self):
        return f"{self.ankit_name}"
d1=Fruit()
d1.ankit_name="Apple"
d1.ankit_get_fruit()
d1.ankit_name="Mango"
d1.ankit_get_fruit()
d1.ankit_name="Banana"
d1.ankit_get_fruit()
```
# Create a Phone class, create two objects, and use type() and isinstance() to verify their type.
```
class Phone:
    def __init__(self,name,age):
        self.ankit_name=name
        self.ankit_age=age
    def get_info(self):
        return f"The type of {self.ankit_name} is {type(self.ankit_name)}."
p1= Phone()
print(type(p1))
print(isinstance(p1,Phone))
```
# Create a Color class with a name attribute. Create two objects, change one's name, and print both to confirm they are independent.
```
# 1. Color class
class Color:
    def __init__(self, name):
        self.name = name

color1 = Color("ankit")
color2 = Color("blue")

color1.name = "red"

print("Color 1:", color1.name)
print("Color 2:", color2.name)

```

# Create a Book class. Create two book objects and give each a title, author, and pages attribute. Print them all.
```
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Book("Python Basics", "Ankit", 250)
book2 = Book("The Alchemist", "Paulo Coelho", 208)

print(book1.title, book1.author, book1.pages)
print(book2.title, book2.author, book2.pages)
```

# Create a Pet class, create an object, set its name and age, then modify the age and print before and after.
```
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

pet1 = Pet("Tommy", 2)

print("Before age change:", pet1.name, pet1.age)

pet1.age = 3

print("After age change:", pet1.name, pet1.age)
```
     
# Create a Product class with two objects. Give each a name, price, and quantity. Print the total value (price times quantity) for each
```
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

product1 = Product("Laptop", 80000, 2)
product2 = Product("Mouse", 1500, 3)

print(product1.name, "total value:", product1.price * product1.quantity)
print(product2.name, "total value:", product2.price * product2.quantity)
```