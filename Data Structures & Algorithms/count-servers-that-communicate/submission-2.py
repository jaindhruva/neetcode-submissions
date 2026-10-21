class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        connectedSet = set()

        def dfs(i, j):
            for x in range(m):
                if x == i:
                    continue
                if grid[x][j] == 1:
                    connectedSet.add((i,j))
                    connectedSet.add((x,j))
            
            for y in range(n):
                if y == j:
                    continue
                if grid[i][y] == 1:
                    connectedSet.add((i,y))
                    connectedSet.add((i,j))
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    if len(connectedSet) == m*n:
                        return m*n
        
        return len(connectedSet)
        