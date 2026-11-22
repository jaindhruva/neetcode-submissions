class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def outOfBound(x,y):
            return (
                x < 0 or x >= n or
                y < 0 or y >= n
            )
        if grid[0][0] != 0 :
            return -1
        q = deque()
        q.append((0,0))
        level = 1
        dirs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        visited = set()
        visited.add((0,0))
        while q:
            size = len(q)
            for _ in range(size):
                x,y = q.popleft()
                if x == n-1 and y == n-1:
                    return level
                for dx,dy in dirs:
                    i = x + dx
                    j = y + dy
                    if not outOfBound(i,j) and (i,j) not in visited and grid[i][j] == 0:
                        q.append((i,j))
                        visited.add((i,j))

            level += 1

        return -1
                