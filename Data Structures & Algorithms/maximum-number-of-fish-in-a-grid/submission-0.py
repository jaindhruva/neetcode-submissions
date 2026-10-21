class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(i,j):
            nonlocal visited
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 0 or (i,j) in visited:
                return 0
                
            visited.add((i,j))
            area = grid[i][j]

            for dx,dy in dirs:
                x = i+dx
                y = j+dy
                if (x,y) not in visited:
                    area += dfs(x,y)

            return area

        maxArea = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                maxArea = max(maxArea,dfs(i,j))

        return maxArea
