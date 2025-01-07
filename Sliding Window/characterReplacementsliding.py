class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        counts = [0] * 26

        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1
            while (r-l+1) - max(counts) > k:
                counts[ord(s[l])-65] -= 1
                l += 1
            
            longest = max(longest, (r-l+1))
        
        return longest
    
class Solution:
    def characterReplacement2(self, s: str, k: int) -> int:
        # dictionary to store count of characters in current window
        counts = {}
        max_length = 0
        max_count = 0
        left = 0

        for right in range(len(s)):
            # adding new character to window
            counts[s[right]] = counts.get(s[right], 0) + 1

            max_count = max(max_count, counts[s[right]])
            
            window_length = right - left + 1
            if window_length - max_count > k:
                counts[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right-left+1)
        
        return max_length