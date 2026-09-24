class Solution:
    def isAlphanumeric(self, c):
        if 'a'<=c<='z' or 'A'<=c<='Z' or '0'<=c<='9':
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l<r:
            while (not self.isAlphanumeric(s[l])) and l<r :
                l += 1
            while (not self.isAlphanumeric(s[r])) and l<r:
                r -= 1
            if(s[l].lower() != s[r].lower()):
                return False
            l += 1
            r -= 1

        return True