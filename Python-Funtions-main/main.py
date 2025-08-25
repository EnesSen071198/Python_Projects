# 1. Function Definition and Call
def greet():
    print("Hello, Python!")
greet()  # Function is called

# 2. Function with Parameters
def add(a, b):
    return a + b
result = add(3, 5)
print(result)  # 8

# 3. Function with Default Parameter Value
def hello(name="Guest"):
    print(f"Hello, {name}!")
hello()        # Hello, Guest!
hello("Enes")  # Hello, Enes!

# 4. Function with Return Value
def multiply(a, b):
    return a * b
result = multiply(4, 6)
print(result)  # 24

# 5. Function with Variable Number of Arguments (*args)
def add(*args):
    return sum(args)
print(add(1, 2, 3))  # 6
print(add(5, 10, 15, 20))  # 50

# 6. Function with Keyword Arguments (**kwargs)
def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
person_info(name="Enes", age=25)
# name: Enes
# age: 25

# 7. Lambda Function
add = lambda a, b: a + b
print(add(3, 5))  # 8

# 8. Calling Functions Inside Functions
def square(x):
    return x * x

def add_and_square(a, b):
    total = a + b
    return square(total)

print(add_and_square(3, 4))  # 49 (7 squared)
