class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(i,open_count,curr):
            if i==(2*n) and open_count==0:
                res.append(curr)
                return
            if open_count < 0 or i>=(2*n):
                return
            if open_count > 0:
                dfs(i+1,open_count-1,curr+')')

            dfs(i+1,open_count+1,curr+'(')


        dfs(0,0,'')
        return res