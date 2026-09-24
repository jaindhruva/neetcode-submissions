class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        curr_valid_rate = r
        while l<=r:
            m = (l+r)//2
            
            rate_time_taken = 0
            for p in piles:
                rate_time_taken += math.ceil(p/m)
            print(m)
            print(rate_time_taken)
            print('-')
            if rate_time_taken <= h:
                curr_valid_rate = m
                r = m-1
            else:
                l = m+1
        return curr_valid_rate