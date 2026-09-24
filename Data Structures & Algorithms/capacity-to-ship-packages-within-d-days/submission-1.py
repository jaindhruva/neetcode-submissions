class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(wt):
            d, curr_wt = 1, wt
            for w in weights:
                if curr_wt - w < 0:
                    d += 1
                    if d > days:
                        return False
                    curr_wt = wt
                curr_wt -= w
            return True
                
        l, r = max(weights), sum(weights)

        min_wt = r
        while l<=r :
            m = l + (r-l)//2
            if canShip(m):
                min_wt = min(min_wt, m)
                r = m - 1
            else:
                l = m + 1
        
        return min_wt
