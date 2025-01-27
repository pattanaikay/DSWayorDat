"""
Given two sorted arrays, write a function that merges them into a single sorted array.

"""

def mergedSortedArrays(arr1:list, arr2:list)->list:
    if not arr1:
        return arr2
    if not arr2:
        return arr1

    merged_array = []
    m, n = 0, 0

    while m < len(arr1) and n < len(arr2):
        if arr1[m] <= arr2[n]:
            merged_array.append(arr1[m])
            m += 1
        else:
            merged_array.append(arr2[n])
            n += 1
    
    merged_array.extend(arr1[m:])
    merged_array.extend(arr1[n:])

    return merged_array

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

print(mergedSortedArrays(arr1, arr2))
