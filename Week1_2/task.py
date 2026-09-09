# 1 Write a program that takes two numbers and prints the result of all 7 arithmetic operations (+, -, *, /, //, %, **).
a_ankit=2
b_ankit=7
print(f'The sum of {a_ankit} and {b_ankit} is {a_ankit+b_ankit}')
print(f'The difference of {a_ankit} and {b_ankit} is {a_ankit-b_ankit}')
print(f'The multiplication of {a_ankit} and {b_ankit} is {a_ankit*b_ankit}')
print(f'The division of {a_ankit} and {b_ankit} is {a_ankit/b_ankit}')
print(f'The floor division of {a_ankit} and {b_ankit} is {a_ankit//b_ankit}')
print(f'The modulor division of {a_ankit} and {b_ankit} is {a_ankit%b_ankit}')
print(f'The exponential of {a_ankit} and {b_ankit} is {a_ankit**b_ankit}')

# 2 Create a tip calculator: take a bill amount and tip percentage, calculate the tip and total.
amount_ankit=455
tip_percent=20
tip_ankit=20/100*amount_ankit
total_ankit=amount_ankit+tip_ankit
print(f'The total is {total_ankit} with tip {tip_ankit}')

# 3 Check if a number is even or odd using the modulus operator (%).
num_ankit=34
if num_ankit%2==0:
  print(f'{num_ankit} is even')
else:  
  print(f'{num_ankit} is odd')

# 4 Ask for the user's name and age, then print: "Hello [name], you are [age] years old."
name_ankit=input('Enter your Name')
age_ankit=input('Enter your age')
print(f"Hello {name_ankit}, you are {age_ankit} years old.")

# 5 Ask for a temperature in Celsius and convert to Fahrenheit using F = C * 9/5 + 32. Display the result with 1 decimal place.
temp_ankit=int(input('Enter the temperature in celcius'))
f_ankit= temp_ankit * 9/5 + 32
print(F'The temperature in fahrenheit is {f_ankit:.1f}')

# 6 Create a formatted receipt: ask for 3 items and their prices, display each item and the total.
i1_ankit=input('Enter the item 1 ')
p1_ankit=int(input('Enter the price of item 1 '))

i2_ankit=input('Enter the item 2 ')
p2_ankit=int(input('Enter the price of item 2 '))

i3_ankit=input('Enter the item 3 ')
p3_ankit=int(input('Enter the price of item 3 '))

t_ankit = p1_ankit+p2_ankit+p3_ankit
print(f'{i1_ankit} has price {p1_ankit}')
print(f'{i2_ankit} has price {p2_ankit}')
print(f'{i3_ankit} has price {p3_ankit}')
print(f'The total price is {t_ankit}')

# 7 Ask for a username and password. Print "Access granted" only if both are correct.
u_ankit=input('Enter your username')
p_ankit=input('Enter your password')
if u_ankit== 'user' and p_ankit == 'password':
  print('Access granted')
else:
  print('Access denied')

# 8 Check if a number is between 1 and 100 (inclusive) using and.
number_ankit=75
if number_ankit < 100 and number_ankit > 1:
   print(f'{number_ankit} is between 1 and 100')

# 9 Write a program that checks if a year is a leap year (divisible by 4 and not 100, or divisible by 400).
y_ankit=2026
if y_ankit%4 == 0 and y_ankit !=100 or y_ankit%400 == 0:
  print(f'{y_ankit} is a leap year')

# 10 Ask the user for a number. Print whether it is positive, negative, or zero.
ankit_num=int(input('Enter the number'))
if ankit_num < 0 :
    print(f'{ankit_num} is negative number')
elif ankit_num > 0:
    print(f'{ankit_num} is positive')
else:
    print(f'{ankit_num} is a zero')

# 11 Write a grading system: take a score (0-100) and print the letter grade (A, B, C, D, or F).
s_ankit=int(input('Enter the score must be between 1 and 100'))
if s_ankit >100 or s_ankit < 0:
    print(f'Invalid Score')
elif s_ankit >= 90:
    print("A")
elif s_ankit >= 80:
    print("B")
elif s_ankit >= 70:
    print("C")
elif s_ankit >= 60:
    print("D")
else:
    print("F")
# 12 Ask for an age and print the ticket price: child (under 12) = $5, adult (12-64) = $10, senior (65+) = $7.
ankit_age=int(input('Enter your age'))
if ankit_age < 0 :
    print('Invalid Age')
elif ankit_age < 12:
    print(f'The ticket price is $5')
elif 12 < ankit_age <64:
    print(f'The ticket price is $10')
else:
    print(f'The ticket price is $7')

# 13 Print the multiplication table for any number (1 to 10) using a for loop.
for i in range(1,11):
    print(f'5 x {i} = {5*i}')

# 14 Loop through a list of 5 names and print each with its position (use enumerate).
names_ankit=['Ankit','Rohit','Saurabh','Ramesh','Rakesh']
for index, name in enumerate(names_ankit):
    print(f'Position {index+1}: {name}')

# 15 Calculate the sum of all even numbers from 1 to 50 using range().
sum_even_ankit=0
for i in range(1,51):
    if i%2==0:
        print(f'{i} is even number')
        sum_even_ankit+=i
print(f'The sum of all even numbers from 1 to 50 is {sum_even_ankit}')





# 22: What exception will occur if a user enters 0 as the divisor? Write a Python program to handle the exception using try and except.
ankit_numerator = 10
ankit_divisor = 0

try:
    ankit_result = ankit_numerator / ankit_divisor
    print(f"The result is: {ankit_result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# 23: Why is the finally block used in Python? Write a program that opens a file, reads its contents, and ensures the file is closed using finally.
ankit_file_name = "ankit_sample.txt"

# Create a dummy file for demonstration
with open(ankit_file_name, "w") as ankit_f:
    ankit_f.write("Hello from the sample file!")

ankit_file_object = None
try:
    ankit_file_object = open(ankit_file_name, "r")
    ankit_content = ankit_file_object.read()
    print(f"File content: {ankit_content}")
except FileNotFoundError:
    print(f"Error: File '{ankit_file_name}' not found.")
finally:
    if ankit_file_object:
        ankit_file_object.close()
        print("File closed successfully in the finally block.")

# 24: When should you use the raise statement in Python? Write a program that raises a ValueError if a student's marks are less than 0 or greater than 100.        
def ankit_set_student_marks(ankit_marks):
    if not isinstance(ankit_marks, (int, float)):
        raise TypeError("Marks must be a number.")
    if ankit_marks < 0 or ankit_marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    print(f"Student marks set to: {ankit_marks}")

try:
    ankit_set_student_marks(85)
    ankit_set_student_marks(-5)
except ValueError as ankit_e:
    print(f"Caught an error: {ankit_e}")

try:
    ankit_set_student_marks(105)
except ValueError as ankit_e:
    print(f"Caught an error: {ankit_e}")

# 25: How can you handle multiple exceptions in a single Python program? Write a program that handles both ZeroDivisionError and IndexError.    
ankit_numbers = [1, 2, 0, 4]
ankit_data_list = [10, 20, 30]

# Scenario 1: ZeroDivisionError
try:
    ankit_index = 2
    ankit_divisor = ankit_numbers[ankit_index]
    ankit_result_div = ankit_data_list[0] / ankit_divisor
    print(f"Division result: {ankit_result_div}")
except ZeroDivisionError:
    print("Error: Division by zero occurred!")
except IndexError:
    print("Error: Index out of bounds occurred!")
except Exception as ankit_e:
    print(f"An unexpected error occurred: {ankit_e}")

print("---------------------")

# Scenario 2: IndexError
try:
    ankit_index = 5
    ankit_value = ankit_data_list[ankit_index]
    print(f"Value at index {ankit_index}: {ankit_value}")
except ZeroDivisionError:
    print("Error: Division by zero occurred!")
except IndexError:
    print("Error: Index out of bounds occurred!")
except Exception as ankit_e:
    print(f"An unexpected error occurred: {ankit_e}")


# 26: What happens if a program tries to open a file that does not exist? Write a
# Python program to handle the exception while reading student.txt . keyboard_arrow_down
ankit_non_existent_file = "student.txt"
try:
   with open(ankit_non_existent_file, 'r') as ankit_file:
     ankit_content = ankit_file.read()
     print(f"Content of {ankit_non_existent_file}:\n{ankit_content}")
except FileNotFoundError:
   print(f"Error: The file '{ankit_non_existent_file}' does not exist.")
except Exception as ankit_e:
   print(f"An unexpected error occurred: {ankit_e}")


# Question 27: Why should the with open() statement be preferred over open() andclose() ? Write a program that reads a text file line by line using with open() . keyboard_arrow_down
ankit_existing_file_name = "ankit_sample_for_q27.txt"
# Create a dummy file for demonstration
with open(ankit_existing_file_name, "w") as ankit_f_write:
  ankit_f_write.write("First line.\n")
  ankit_f_write.write("Second line.\n")
  ankit_f_write.write("Third line.\n")
  print(f"Reading file '{ankit_existing_file_name}' line by line using 'with open()':")
try:
  with open(ankit_existing_file_name, 'r') as ankit_file_read:
    for ankit_line_num, ankit_line in enumerate(ankit_file_read):
      print(f"Line {ankit_line_num + 1}: {ankit_line.strip()}")
except FileNotFoundError:
   print(f"Error: The file '{ankit_existing_file_name}' was not found.")
except Exception as ankit_e:
   print(f"An unexpected error occurred: {ankit_e}")    


#  28: When should you use append mode ('a') while writing to a file? Write a Python
# program that adds a new employee record to employee.txt without deleting the existing
# data.
ankit_employee_file = "employee.txt"
# Initialize the file with some existing data if it doesn't exist or is empty
with open(ankit_employee_file, 'w') as ankit_file_init:
   ankit_file_init.write("ID,Name,Department\n")
   ankit_file_init.write("101,Ankit Sharma,Sales\n")
   ankit_new_employee = "102,Ankit Patel,Marketing\n"
   print(f"Current content of '{ankit_employee_file}':")
try:
    with open(ankit_employee_file, 'r') as ankit_file_read:
      print(ankit_file_read.read().strip())
# Add a new record using append mode
    with open(ankit_employee_file, 'a') as ankit_file_append:
       ankit_file_append.write(ankit_new_employee)
       print("\nNew employee added successfully.")
       print(f"Updated content of '{ankit_employee_file}':")
    with open(ankit_employee_file, 'r') as ankit_file_read_updated:
       print(ankit_file_read_updated.read().strip())
except IOError as ankit_io_error:
    print(f"Error accessing file: {ankit_io_error}")
except Exception as ankit_e:
    print(f"An unexpected error occurred: {ankit_e}")


# Question 29: How can you copy the contents of one file to another in Python? Write a program
# to copy data from source.txt to destination.txt while handling file-related exceptions. keyboard_arrow_down
ankit_source_file = "source.txt"
ankit_destination_file = "destination.txt"
# Create a dummy source file for demonstration
with open(ankit_source_file, 'w') as ankit_f_source_write:
    ankit_f_source_write.write("This is the content from the source file.\n")
    ankit_f_source_write.write("It has multiple lines of text.\n")
    print(f"Copying content from '{ankit_source_file}' to '{ankit_destination_file}'...")
try:
    with open(ankit_source_file, 'r') as ankit_src:
      with open(ankit_destination_file, 'w') as ankit_dest:
         ankit_dest.write(ankit_src.read())
         print("File copied successfully.")
         print(f"Content of '{ankit_destination_file}':")
    with open(ankit_destination_file, 'r') as ankit_dest_read:
       print(ankit_dest_read.read().strip())
except FileNotFoundError:
    print(f"Error: Either '{ankit_source_file}' or '{ankit_destination_file}' was not found.")
except IOError as ankit_io_error:
    print(f"Error during file operation: {ankit_io_error}")
except Exception as ankit_e:
    print(f"An unexpected error occurred: {ankit_e}")
