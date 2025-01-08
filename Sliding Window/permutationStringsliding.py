class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        # create character count arrays
        s1_count  = {}
        window_count = {}

        # count characters in s1
        for char in s1:
            s1_count[char] =  s1_count.get(char, 0) + 1
        
        # initialize the first window
        for i in range(len(s1)):
            char = s2[i]
            window_count[char] = window_count.get(char, 0) + 1

        # compare the first window
        if window_count == s1_count:
            return True

        # slide windows
        for i in range(len(s1), len(s2)):
            newchar = s2[i]
            window_count[newchar] = window_count.get(newchar, 0) + 1

            # remove the old characters
            oldchar = s2[i-len(s1)]
            window_count[oldchar] -= 1
            if window_count[oldchar] == 0:
                del window_count[oldchar]

            if window_count == s1_count:
                return True
        
        return False