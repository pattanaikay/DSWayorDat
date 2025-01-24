"""
Write a function that takes a list of integers and returns the second largest number in the list.

"""

def secondLargestNumber(nums):
    if len(nums)<2:
        return None
    
    firstMax = secondMax = float('-inf')

    for num in nums:
        if num > firstMax:
            secondMax = firstMax
            firstMax = num
        elif num > secondMax and num != firstMax:
            secondMax = num

    return secondMax

n = [7, 1, 3, 5, 8, 4]

print(secondLargestNumber(n))

    