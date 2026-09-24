class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(i, j, area):
            if i<0 or i>=m or j<0 or j>=n or (i,j) in visited or grid[i][j]==0:
                return area
            visited.add((i,j))
            area = (1 +  dfs(i+1,j,0) +
                        dfs(i-1,j,0) + 
                        dfs(i,j+1,0) + 
                        dfs(i,j-1,0))
            return area


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    maxArea = max(maxArea, dfs(i,j,0))
        
        return maxArea