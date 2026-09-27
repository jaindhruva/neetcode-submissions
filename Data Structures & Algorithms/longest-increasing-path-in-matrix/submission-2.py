class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_len = 0
        m, n = len(matrix), len(matrix[0])
        dp = {}

        def dfs(i,j,prev):
            if i not in range(m) or j not in range(n) or prev >= matrix[i][j]:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]

            res = 1

            res = max(res,
                      1 + dfs(i+1,j,matrix[i][j]),
                      1 + dfs(i-1,j,matrix[i][j]),
                      1 + dfs(i,j+1,matrix[i][j]),
                      1 + dfs(i,j-1,matrix[i][j]))
            
            dp[(i,j)] = res
            return res
        

        for i in range(m):
            for j in range(n):
                max_len = max(max_len, dfs(i,j,-1))
            
        return max_len
            
