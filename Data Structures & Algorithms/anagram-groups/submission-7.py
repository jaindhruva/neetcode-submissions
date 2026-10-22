class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            count = [0]*26
            s2 = sorted(s)
            anagram_map[str(s2)].append(s)
            
        return list(anagram_map.values())