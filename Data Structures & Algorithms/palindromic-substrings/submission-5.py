class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = set()
        def isPalindrome(s):
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            dp.add(s)
            return True


        count = len(s)
        for size in range(2, len(s)+1):
            for i in range(0, len(s)-size+1):

                if s[i:i+size] in dp or isPalindrome(s[i:i+size]):
                    count += 1

        return count