# In this short lesson, we will be going over functions, and how they are written/used in Python.
# 
# What is a function?
# 
# A block of code which can only be executed once its invoked (called).
# To define a function in Python, we use the [def] keyword, followed by the name of your function.
# Functions in Python can run blocks of code, and also return answers from the code its ran.
#                       
# An example function that returns a string can be seen defined here:
def string_return():
  myString = "Hello, World"
  return myString
         

# Task 1: Define a function called my_function that prints "Hello, World", and doesn't return anything.
def my_function():
    print("Hello, World")

# Task 2: Define another function called my_function2 that returns the sum 10 & 8.
# Hint: To return the answer, simply use the "return" keyword.
def my_function2():
    return None

def main():
    # Call my_function()
    my_function()
    # Call my_function2()
    print(my_function2())