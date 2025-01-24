"""
 Given a list of numbers, write a Python function to find the median.

"""

def searchMedian(nums):
    if not nums:
        return None
    
    nums.sort()
    mid = len(nums) //2

    if len(nums) % 2 == 0:
        return (nums[mid-1]+nums[mid])/2
    else:
        return nums[mid]
