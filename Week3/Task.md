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
ankit_student3_name = "Charlie"
ankit_student3_age = 17
ankit_student3_grade = "A-"

print("Procedural Student Data:")
print(f"Student 1: {ankit_student1_name}, Age: {ankit_student1_age}, Grade: {ankit_student1_grade}")
print(f"Student 2: {ankit_student2_name}, Age: {ankit_student2_age}, Grade: {ankit_student2_grade}")
print(f"Student 3: {ankit_student3_name}, Age: {ankit_student3_age}, Grade: {ankit_student3_grade}")

# How OOP would handle it:
# In an OOP approach, we would define a 'Student' class with attributes like name, age, and grade.
# Each student would be an 'object' (instance) of this class. Adding a new student means creating a new instance.
# This makes the code cleaner, more organized, and easier to scale as the number of students or attributes grows.

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

# Create a class called Book with attributes title, author, and pages.

# Create a class called Movie with attributes for title, director, and year.

# Create a class called PhoneContact with attributes for name, phone number, and email. Print each attribute.