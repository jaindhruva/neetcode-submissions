class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        dp = [[0]*(n+1) for _ in range(m+1)] 
        # dp array symbolizes at (i,j) is number of substrings of t[j:]  in s[i:]

        for i in range(m+1):
            dp[i][n] = 1
            # for empty string we have 1 match
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = dp[i+1][j] # every substring in s will at least have same no of possible substrings as that of the substring from the next element

                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1] # in case there's a match of chars , then this will have additional possible substrings of bottom right neighbor
        

        return dp[0][0]