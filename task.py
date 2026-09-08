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
# 15 Calculate the sum of all even numbers from 1 to 50 using range().