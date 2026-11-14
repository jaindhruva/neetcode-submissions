import sys

sys.setrecursionlimit(20000)

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        unsafe_set = set()
        visited = set()
        n = len(graph)

        def dfs(i, path_set):
            visited.add(i)
            for nbr in graph[i]:
                if nbr in path_set or nbr in unsafe_set:
                    unsafe_set.update(path_set)
                    return 
                path_set.add(nbr)
                dfs(nbr, path_set)
                path_set.remove(nbr)
            
        for i in range(n):
            if i not in visited:
                visited.add(i)
                path_set = set()
                path_set.add(i)
                dfs(i,path_set)
        
        res = []
        for i in range(n):
            if i not in unsafe_set:
                res.append(i)

        return res