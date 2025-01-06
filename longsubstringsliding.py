class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = maxL = 0

        for right, char in enumerate(s):
            if char in seen and seen[char]>=left:
                left = seen[char] + 1
            else:
                maxL = max(maxL, right-left+1)
            
            seen[char] = right
        
        return maxL