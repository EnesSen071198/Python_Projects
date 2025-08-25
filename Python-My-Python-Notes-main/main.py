# For single-line comments, use the '#' symbol
# These comments explain what the code does

'''
For multi-line comments, use triple quotes
This way you can write multiple lines
'''

# ----- Data Types -----

# String data type
name = "Ahmet"  # Strings are written inside double quotes
surname = 'Yılmaz'  # Single quotes can also be used
print("Name:", name)  # Name: Ahmet

# Integer data type
age = 25  # Integers are written directly
birth_year = 1998
print("Age:", age)  # Age: 25

# Float data type
height = 1.78  # Use a dot for decimal numbers
weight = 70.5
print("Height:", height)  # Height: 1.78

# Boolean data type
is_married = False  # Takes True or False
is_student = True
print("Is student?:", is_student)  # Is student?: True

# Using type() to check data type
print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_married)) # <class 'bool'>

# ----- Type Conversions -----

# String to Integer
num_str = "123"
num = int(num_str)
print("Converted number:", num + 5)  # 128

# Integer to String
number = 42
number_str = str(number)
print("As text: " + number_str)  # As text: 42

# ----- Mathematical Operators -----

# Addition (+)
n1 = 10
n2 = 5
total = n1 + n2
print(f"Sum: {total}")  # Sum: 15

# Subtraction (-)
diff = n1 - n2
print(f"Difference: {diff}")  # Difference: 5

# Multiplication (*)
product = n1 * n2
print(f"Product: {product}")  # Product: 50

# Division (/)
division = n1 / n2
print(f"Division: {division}")  # Division: 2.0 (always float)

# Integer division (//)
int_division = n1 // n2
print(f"Integer division: {int_division}")  # Integer division: 2

# Modulus (%)
remainder = n1 % n2
print(f"Remainder: {remainder}")  # Remainder: 0

# Exponentiation (**)
power = n1 ** 2
print(f"Square of 10: {power}")  # Square of 10: 100

# ----- Comparison Operators -----

x = 10
y = 5

print(f"{x} == {y}: {x == y}")  # Equal to: False
print(f"{x} != {y}: {x != y}")  # Not equal: True
print(f"{x} > {y}: {x > y}")    # Greater than: True
print(f"{x} < {y}: {x < y}")    # Less than: False
print(f"{x} >= {y}: {x >= y}")  # Greater or equal: True
print(f"{x} <= {y}: {x <= y}")  # Less or equal: False

# ----- Logical Operators -----

a = True
b = False
print(f"True and False: {a and b}")  # False
print(f"True or False: {a or b}")    # True
print(f"not True: {not a}")          # False

# ----- Conditional Statements -----

age = 18
if age >= 18:
    print("You are an adult")

temperature = 25
if temperature > 30:
    print("It's hot")
else:
    print("It's not hot")

score = 85
if score >= 90:
    print("AA")
elif score >= 80:
    print("BA")
elif score >= 70:
    print("BB")
else:
    print("CC")

# Nested if
username = "admin"
password = "1234"
if username == "admin":
    if password == "1234":
        print("Login successful!")
    else:
        print("Wrong password!")
else:
    print("Wrong username!")

# ----- Loops -----

# For loop - list iteration
fruits = ["apple", "pear", "banana"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# For loop with range
for i in range(3):  # 0 to 2
    print(f"Number: {i}")

# While loop
counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1

# Break
for i in range(5):
    if i == 3:
        break
    print(i)

# Continue
for i in range(4):
    if i == 2:
        continue
    print(i)

# ----- Lists -----
fruits = ["apple", "pear", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]

print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"First two fruits: {fruits[0:2]}")

fruits.append("grape")
fruits.insert(1, "orange")
fruits.remove("pear")
fruits.pop()
print(len(fruits))

# ----- Tuples -----
coordinates = (3, 5)
colors = ("red", "blue", "green")
print(colors.count("blue"))
print(colors.index("green"))

# ----- Dictionaries -----
student = {
    "name": "Ahmet",
    "surname": "Yılmaz",
    "age": 20,
    "courses": ["Math", "Physics"]
}
print(student["name"])
print(student.get("average", "No data"))
student["department"] = "Computer Engineering"
del student["age"]

# ----- Functions -----
def greet():
    print("Hello!")

def greet_person(name):
    print(f"Hello {name}!")

def greet_lang(name, lang="EN"):
    if lang == "EN":
        print(f"Hello {name}!")
    elif lang == "TR":
        print(f"Merhaba {name}!")

def add(a, b):
    return a + b

# ----- Try-Except -----
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid number!")

# ----- File Handling -----
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Learning Python\n")

# ----- Modules -----
import math, random
from datetime import datetime, timedelta

print(math.pi)
print(random.randint(1, 10))
print(datetime.now())

# ----- OOP -----
class Car:
    count = 0
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.count += 1
    def accelerate(self, amount):
        print(f"Speed increased by {amount}")

class ElectricCar(Car):
    def charge(self):
        print("Battery fully charged")

# ----- Decorators -----
def time_it(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f"{func.__name__} took {end - start}")
        return result
    return wrapper

# ----- List Comprehension -----
squares = [i**2 for i in range(5)]
evens = [i for i in range(10) if i % 2 == 0]
