class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_map = {}
        for c in s:
            if c not in count_map:
                count_map[c] = 0
            count_map[c] += 1
        
        for c in t:
            if c not in count_map:
                return False
            count_map[c] -= 1
            if count_map[c] == 0:
                count_map.pop(c)
        
        if len(count_map) > 0:
            return False

        return True