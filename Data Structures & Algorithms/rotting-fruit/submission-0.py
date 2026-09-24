class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, t = 0, 0
        q = collections.deque()
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        while fresh > 0 and q:
            l = len(q)
            for i in range(l):
                x,y = q.popleft()
                
                for dir in dirs:
                    new_x, new_y = x+dir[0], y+dir[1]
                    if new_x in range(rows) and new_y in range(cols) and grid[new_x][new_y] == 1:
                        q.append((new_x, new_y))
                        grid[new_x][new_y] = 2
                        fresh -= 1
            t += 1
        
        return t if fresh == 0 else -1