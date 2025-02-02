"""
Define a sample decorator functions

A decorator is a higher-order function that takes another function as an argument and returns a new function.

"""

def myDecorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called")
        result = func(*args, **kwargs)
        print("After the function is called")

        return result
    
    return wrapper

@myDecorator
def greet():
    print("Hello, world!")

greet()