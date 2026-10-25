class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def expand(l, r):
            total = 0

            while l>=0 and r<len(s) and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1
            
            return total
        
        count = 0
        for i in range(len(s)):
            count += expand(i, i) # odd
            count += expand(i, i+1) # event

        return count

