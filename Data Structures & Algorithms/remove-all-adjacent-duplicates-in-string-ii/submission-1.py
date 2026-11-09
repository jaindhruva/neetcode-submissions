class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        l = r = 0
        while l < len(s) - k + 1 and r < len(s):
            if s[l] == s[r]:
                if r-l+1 == k:
                    s = s[0:l] + s[r+1:]
                    l = max(0,l-k)
                    r = l
                    continue
                r += 1
            else:
                l += 1
                r = l+1

        return s
