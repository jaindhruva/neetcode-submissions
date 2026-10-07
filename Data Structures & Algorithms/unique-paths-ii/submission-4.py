class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for i in range(m)]

        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        dp[0][0] = 1
        # top row, i=0
        i = 0
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i][j-1]
        
        # left row, j=0
        j = 0
        for i in range(1, m):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i-1][j]
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        

        return dp[m-1][n-1]