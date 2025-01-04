class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        currmax = currmin = globalmax = nums[0]

        for n in nums[1:]:
            prev_max = currmax

            currmax = max(n, currmax * n, currmin * n)
            currmin = min(n, prev_max * n, currmin * n)

            globalmax = max(globalmax, currmax)
        
        return globalmax