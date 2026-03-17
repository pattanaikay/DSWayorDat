class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_check = set()
        for n in nums:
            if n in num_check:
                return True
            num_check.add(n)
        return False