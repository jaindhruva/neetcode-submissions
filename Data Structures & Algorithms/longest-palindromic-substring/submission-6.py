class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen, resIndex = 0, 0
        n = len(s)
        for i in range(n):
            # odd palindromes
            l = r = i
            while l in range(n) and r in range(n) and s[l] == s[r]:
                if r-l+1 > resLen :
                    resLen = r-l+1
                    resIndex = l    
                l -= 1
                r += 1

            # even palindromes
            l, r = i, i+1
            while l in range(n) and r in range(n) and s[l] == s[r]:
                if r-l+1 > resLen :
                    resLen = r-l+1
                    resIndex = l    
                l -= 1
                r += 1

        return s[resIndex: resIndex+resLen]