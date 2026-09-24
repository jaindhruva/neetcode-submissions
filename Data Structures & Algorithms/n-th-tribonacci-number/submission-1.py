class Solution:
    def tribonacci(self, n: int) -> int:
        prev3, prev2, prev1 = 0,1,1
        res = 0
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        for i in range(3,n+1):
            res = prev3 + prev2 + prev1
            prev3 = prev2
            prev2 = prev1
            prev1 = res
        
        return res