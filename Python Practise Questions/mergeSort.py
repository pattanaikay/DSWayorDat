"""
Sorts the given array in ascending order using the merge sort algorithm.

"""

def performMergeSort(nums:list)->list:
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left_index)
            left_index += 1
        else:
            merged.append(right_index)
            right_index += 1
    
    merged.append(left[left_index:])
    merged.append(right[right_index:])

    return merged