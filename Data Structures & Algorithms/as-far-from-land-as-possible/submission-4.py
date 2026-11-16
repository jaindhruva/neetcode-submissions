from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        res = -1
        m, n = len(grid), len(grid[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i,j))

        def out_of_bounds(i,j):
            return (
                i < 0 or j < 0 or
                i >= m or j >= n
            )

        while q:
            i,j = q.popleft()
            res = grid[i][j]
            nbrs  = [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]
            for nx,ny in nbrs:
                if not out_of_bounds(nx, ny) and grid[nx][ny]==0:
                    q.append((nx,ny))
                    grid[nx][ny] = 1 + grid[i][j]
        
        return res-1 if res > 1 else -1
