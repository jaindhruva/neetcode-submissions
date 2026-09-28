class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            count = [0]*26
            # s2 = s.clone()
            sorted(s)
            for c in s:
                count[ord(c)-ord('a')] += 1
            anagram_map[tuple(count)].append(s)
            
        return list(anagram_map.values())