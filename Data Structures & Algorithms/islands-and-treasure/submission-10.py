class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        m, n = len(grid), len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        dist = 0
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        
        while q:
            size = len(q)
            for k in range(size):
                i,j = q.popleft()
                grid[i][j] = dist
                for x,y in dirs:
                    x += i
                    y += j
                    if 0<=x<m and 0<=y<n and (x,y) not in visited and grid[x][y] > 0:
                        q.append((x,y))  
                        visited.add((x,y))          
            dist += 1
                


        # return grid
