class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        connectedSet = set()


        # traverse horizontally
        for i in range(m):
            rowSet = set()
            for j in range(n):
                if grid[i][j] == 1:
                    rowSet.add((i,j))
            if len(rowSet) > 1:
                connectedSet.update(rowSet)

        
        # traverse vertically
        for j in range(n):
            colSet = set()
            for i in range(m):
                if grid[i][j] == 1:
                    colSet.add((i,j))
            if len(colSet) > 1:
                connectedSet.update(colSet)
        
        return len(connectedSet)
        