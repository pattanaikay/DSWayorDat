"""
Problem: Create a generator function that yields all possible pairs of numbers
from two lists whose sum is less than a given threshold.

Example:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
threshold = 7

Should yield pairs like: (1,4), (1,5), (2,4), etc.
"""

def generatorFunction(arr1:list, arr2:list, threshold:int)->tuple:
    for x in arr1:
        for y in arr2:
            if (x + y) < threshold:
                yield(x, y)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
threshold = 7
testValue = generatorFunction(list1, list2, threshold)
print(list(testValue))