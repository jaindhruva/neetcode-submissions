class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for x in range(m+1)]
        maxSide = 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + min( dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
                    maxSide = max(maxSide, dp[i][j])
        
        return maxSide*maxSide