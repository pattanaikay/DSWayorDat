class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        currSum = maxSum = nums[0]

        for num in nums[1:]:
            currSum = max(num, num + currSum)
            maxSum = max(currSum, maxSum)

        return maxSum