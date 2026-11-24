from collections import defaultdict
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colour = [0]*len(graph)

        def bfs(i):
            if colour[i]:
                return True
            
            q = deque()
            q.append(i)
            colour[i] = -1
            while q:
                node = q.popleft()
                for nbr in graph[node]:
                    if colour[nbr] == colour[node]:
                        return False
                    
                    
                    if not colour[nbr]:
                        # append if not been visited
                        q.append(nbr)
                        colour[nbr] = -1*colour[node]
            return True


        

        for i in range(len(graph)):
            if not bfs(i):
                return False
        
        return True

