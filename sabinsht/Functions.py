#Functions Example
#Function Defination
def sum(num1, num2):
    sum = num1+num2
    return sum

number1=20
number2=30
total = sum(number1, number2)
print(f"The total of {number1} and {number2} is {total}")

#Python Default Arguments
#Function arguments can have default values in Python.
#We can provide a default value to an argument by using the assignment operator (=).
# Here is an example.
def sum1(num1, num2=10):
    sum = num1+num2
    return sum
total = sum1(30)
print(f"The total is {total}")

def greet(name):
    #docstring
    """
    This function greets to
    the person passed in as
    a parameter
    """
    #functions statements
    print("Hello, " + name + ". Good morning!")

def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""
    if num >= 0:
        return num
    else:
        return -num
print(absolute_value(2))
print(absolute_value(-5))

#variable Scope

def my_func():
    x = 10
    print("Value inside function:",x)
x = 20
my_func()
print("Value outside function:",x)

#Python Arbitrary Arguments
def greet(*names):
    """This function greets all
    the person in the names tuple."""
    # names is a tuple with arguments
    for name in names:
        print("Hello", name)
greet("Monica", "Luke", "Steve", "John")

#nonlocal variable
#This means that the variable can be neither in the local nor the global scope.
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

#Changing Global Variable From Inside a Function using global
c = 0 # global variable
def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)
