class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        m, n = len(maze), len(maze[0])

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(curr):
            if (curr[0],curr[1]) in visited:
                return False
            
            if curr == destination:
                return True
            
            visited.add((curr[0],curr[1]))

            for dir in dirs:
                i = curr[0]
                j = curr[1]

                # move in one dir
                while i in range(m) and j in range(n) and maze[i][j] == 0:
                    i += dir[0]
                    j += dir[1]
                
                if dfs([i-dir[0],j-dir[1]]):
                    return True
            return False
        
        return dfs(start)

            



