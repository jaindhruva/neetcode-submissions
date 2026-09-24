class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        my_set = set()
        max_len = 0
        while r < len(s):
            if s[r] not in my_set:
                my_set.add(s[r])
                r += 1
                max_len = max(max_len, r-l)
            else:
                my_set.remove(s[l])
                l += 1
        
        return max_len