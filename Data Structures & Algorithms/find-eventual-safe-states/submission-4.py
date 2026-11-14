import sys

sys.setrecursionlimit(20000)

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0]*n
        # 0 - not visited
        # 1 - visiting
        # 2 - safe
        # 3 - unsafe

        def dfs(i):
            if state[i] == 1 or state[i] == 3:
                return False
            if state[i] == 2:
                return True
            state[i] = 1
            for nbr in graph[i]:
                if not dfs(nbr):
                    state[i] = 3
                    return False
            
            # not a single nbr is unsafe -> this is safe
            state[i] = 2
            return True
        
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)

        return res