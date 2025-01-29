"""
Given two arrays, write a python function to return the intersection of the two? For example, X = [1,5,9,0] and Y = [3,0,2,9] it should return [9,0]

"""

def intersectionArray(arr1:list, arr2:list)->list:
    arr3 = set(arr1).intersection(set(arr2))
    return arr3

X = [1,5,9,0]
Y = [3,0,2,9]

print(intersectionArray(X, Y))