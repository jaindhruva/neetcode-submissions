class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        dp = {}
        
        def dfs(x,y):
            if x + y == 0:
                return 0
            if x + y == 2:
                return 2
            if (x,y) in dp:
                return dp[(x,y)]

            dp[(x,y)] =  min(dfs(abs(x-1),abs(y-2)), dfs(abs(x-2),abs(y-1)))+1

            return dp[(x,y)]

        return dfs(abs(x), abs(y))