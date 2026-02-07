import math
# Function to calculate area and circumference of a circle
def arcs_0f_circle(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    print("Area of the circle:", area)
    print("Circumference of the circle:", circumference)

# Recursive function to calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Reversing a string
def reverse_string(text):
    reversed_text = text[::-1]
    print("Reversed string:", reversed_text)


# Function to check if a number is even or odd
def even_or_odd(num):
    """This function finds even or odd"""
    if num % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")

# Greeting function
def greet(name):
    print(f"Hello {name} Welcome To the paradise")

# Mathematical Function

def addition(a,b):
    return f"The addition of{a} and {b} is: ", a + b
def subtraction(a,b):
    return f"The subtraction of{a} and {b} is: ", a - b
def multiplication(a,b):
    return f"The multiplication of{a} and {b} is: ", a * b
def division(a,b):
    if b == 0:
        return "Error! Division by zero."
    return f"The division of{a} and {b} is: ", a / b