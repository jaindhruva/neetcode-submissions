class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[-1])

        dp = [[0]*n for x in range(m)]

        for j in range(n):
            dp[m-1][j] = triangle[m-1][j]
        
        for i in range(m-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        
        return dp[0][0]