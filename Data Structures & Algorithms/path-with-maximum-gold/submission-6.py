class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxGold = 0

        def dfs(i, j, sum, visited):
            print(i, j, sum, visited)
            if i<0 or i>=m or j<0 or j>=n or (i,j) in visited or grid[i][j] == 0:
                return 
            
            visited.add((i,j))

            sum += grid[i][j]
            nonlocal maxGold
            maxGold = max(maxGold, sum)

            dfs(i-1, j, sum, visited)
            dfs(i, j+1, sum, visited)
            dfs(i, j-1, sum, visited)
            dfs(i+1, j, sum, visited)
            
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j, 0, set())

        return maxGold
