class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def kokospeed(k):
            hours = 0

            for p in piles:
                hours += ceil(p/k)

            return hours <= h
        
        l, r = 1, max(piles)
        while l < r:
            mid = l + (r-l) // 2
            if kokospeed(mid):
                r = mid
            else:
                l = mid + 1
            
        return l