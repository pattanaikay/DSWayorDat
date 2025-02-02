"""
Find the third highest number in an array

"""

def thirdLargest(nums:list)->int:
    if len(nums) <3:
        return None
    
    firstLargest = nums[0]
    secondLargest = float('-inf')
    thirdLargest = float('-inf')

    for num in nums:
        if num > firstLargest:
            thirdLargest = secondLargest
            secondLargest = firstLargest
            firstLargest = num
        elif num > secondLargest and num < firstLargest:
            thirdLargest = secondLargest
            secondLargest = num
        elif num > thirdLargest and num < secondLargest:
            thirdLargest = num

    return thirdLargest