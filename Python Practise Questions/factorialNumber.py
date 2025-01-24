"""
Write a Python function to calculate the factorial of a number.

"""

def factorialNumber(num):
    if num < 0:
        raise ValueError("num must be non-negative")
    if num == 0:
        return 1
    else:
        return num * factorialNumber(num-1)
    
