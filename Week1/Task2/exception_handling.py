## Exception try ,except block
try:
    a=b
except:
    print("The variable has not been assigned")


## Specific Exception Handling
try:
    result=1/0
except ZeroDivisionError as ex:
    print(ex)
    print("Please enter the denominator greater than 0")

## Multiple Exception Handling
try:
    result=1/2
    a=b
except ZeroDivisionError as ex:
    print(ex)
    print("Please enter the denominator greater than 0")
except Exception as ex1:
    print(ex1)
    print('Main exception got caught here')


## Handling Multiple Exceptions in a single except block
try:
    num=int(input("Enter a number"))
    result=10/num
except ValueError:
    print("This is not a valid number")
except ZeroDivisionError:
    print("enter denominator greater than 0")
except Exception as ex:
    print(ex)


## try,except,else block
try:
    num=int(input("Enter a number:"))
    result=10/num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as ex:
    print(ex)
else:
    print(f"the result is {result}")


## try,except,else and finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as ex:
    print(ex)
else:
    print(f"The result is {result}")
finally:
    print("Execution complete.")
