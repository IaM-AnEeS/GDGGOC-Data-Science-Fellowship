def even_or_odd(num):
    """This function finds even or odd"""
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")
even_or_odd(eval(input("Enter a number:")))

## function with multiple parameters
def add(a,b):
    return a+b

result=add(2,4)
print(result)

## Default Parameters
def greet(name):
    print(f"Hello {name} Welcome To the paradise")

greet("Anees Ahmad")

### Variable Length Arguments // It means the function can take any number of arguments.There are two types of variable length arguments.
## Positional And Keywords arguments

# Positional Arguments
def print_numbers(*args):
    for arg in args:
        print(arg)
print_numbers(1,2,3,4,5,6,7,8,"Anees Ahmad")

# Keyword Arguments
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_details(name="Anees Ahmad",age="23",country="Pakistan")

# Difference between args and kwargs
# Order matters in possitional arguments but not in keyword arguments.