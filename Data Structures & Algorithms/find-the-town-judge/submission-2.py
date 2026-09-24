class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map, trusted_map = {}, {}
        for e in trust:
            if e[0] not in trust_map:
                trust_map[e[0]] = []
            trust_map[e[0]].append(e[1])
            if e[1] not in trusted_map:
                trusted_map[e[1]] = []
            trusted_map[e[1]].append(e[0])
        print(trust_map)
        print(trusted_map)

        for i in range(1,n+1):
            if (i not in trust_map) and (i in trusted_map) and (len(trusted_map[i])==n-1):
                return i
        
        return -1
            