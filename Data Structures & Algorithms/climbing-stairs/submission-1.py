class Solution:
    def climbStairs(self, n: int) -> int:
        count = []
        count.append(1)
        count.append(2)

        for i in range(2,n):
            count.append(count[i-1]+count[i-2])
        
        return count[n-1]