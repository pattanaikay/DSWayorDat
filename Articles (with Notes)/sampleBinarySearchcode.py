# from the article: https://leetcode.com/discuss/post/786126/python-powerful-ultimate-binary-search-t-rwv8/

# isBadVersion API example

isBadVersion = False

class Solution:
    def firstBadVersion(self, n)->int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left =  mid + 1
        return left
    
# search insert text

class Solution:
    def searchInsert(self, nums: list[int], target:int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) //2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left