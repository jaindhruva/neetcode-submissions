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
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        while q:
            size = len(q)
            for i in range(size):
                x,y = q.popleft()
                grid[x][y] = dist
                for dir in dirs:
                    x2 = x + dir[0]
                    y2 = y + dir[1]
                    if 0<=x2<m and 0<=y2<n and grid[x2][y2] > 0 and ((x2,y2) not in visited):
                        q.append((x2,y2))
                        visited.add((x2,y2))
            dist += 1

