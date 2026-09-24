class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        def getCountMap(s):
            count_map = defaultdict(int)
            for c in s:
                count_map[c] += 1
            return count_map
        
        count_map1 = getCountMap(s1)

        window = len(s1)
        for i in range(len(s2)-window+1):
            subString = s2[i:i+window]
            if count_map1 == getCountMap(subString):
                return True
        
        return False
