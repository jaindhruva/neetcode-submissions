class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        res = -1
        for i in range(len(s)):
            if count[s[i]] == 1:
                res = i
                break
        
        return res
            