class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        atl_flow, pac_flow = set(), set()

        def dfs(i,j,prev,ocean):
            if i<0 or i>=m or j<0 or j>=n or ((i,j) in ocean) or heights[i][j]<prev:
                return
            ocean.add((i,j))
            dfs(i+1,j,heights[i][j],ocean)
            dfs(i-1,j,heights[i][j],ocean)
            dfs(i,j+1,heights[i][j],ocean)
            dfs(i,j-1,heights[i][j],ocean)

        
        for i in range(m):
            dfs(i,0,0,pac_flow)
            dfs(i,n-1,0,atl_flow)
        
        for j in range(n):
            dfs(0,j,0,pac_flow)
            dfs(m-1,j,0,atl_flow)
        
        res = []
        for x,y in pac_flow:
            if (x,y) in atl_flow:
                res.append([x,y])

        return res

