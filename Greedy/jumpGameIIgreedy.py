class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        jumps = 0
        currentMaxReach = 0
        nextMaxReach = 0

        for i in range(len(nums)-1):
            nextMaxReach = max(nextMaxReach, i + nums[i])

            if i == currentMaxReach:
                jumps += 1
                currentMaxReach = nextMaxReach

        return jumps