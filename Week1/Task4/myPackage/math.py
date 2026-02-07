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

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def square(n):
    return n * n

def cube(n):
    return n * n * n

def power(base, exponent):
    return base ** exponent
