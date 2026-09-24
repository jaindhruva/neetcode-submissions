class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i in range(0, min(len(word1), len(word2))):
            res.append(word1[i])
            res.append(word2[i])
        if len(word1) < len(word2):
            res.extend(word2[len(word1):])
        elif len(word1) > len(word2):
            res.extend(word1[len(word2):])
            
        return ''.join(res)