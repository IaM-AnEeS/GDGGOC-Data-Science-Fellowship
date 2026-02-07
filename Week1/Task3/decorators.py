### function copy
### closures
### decorators

## function copy
def welcome():
    return "Welcome to the advanced python course"

welcome()

wel=welcome 
print(wel())
del welcome  # as u can see after deleting the original function name we can still call it using the copied name
print(wel())


##closures functions 
# a function defined inside another function and the inner function has access to the outer function's variables even after the outer function has finished executing

def main_welcome(func):
   
    def sub_welcome_method():
        print("Welcome to the GDGGOC-Data-Science-Fellowship")
        func("Welcome everyone to this Task")
        print("Please learn these concepts properly")
    return sub_welcome_method()
main_welcome(print)

### Decorator 
# a special type of closure that modifies the behavior of a function or method. Decorators are often used to add functionality to existing code in a clean and maintainable way.

def main_welcome(func):
   
    def sub_welcome_method():
        print("Welcome to the advance python course")
        func()
        print("Please learn these concepts properly")
    return sub_welcome_method()

@main_welcome
def coure_introduction():
    print("This is an advanced python course")