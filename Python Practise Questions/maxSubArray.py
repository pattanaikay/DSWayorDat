"""

Maximum Subarray Sum (Kadane’s Algorithm). Find the contiguous subarray with the largest sum.

"""

def maxsubArray(nums:list)->int:
    max_sum = curr_sum = nums[0]

    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(curr_sum, max_sum)
    
    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxsubArray(arr))