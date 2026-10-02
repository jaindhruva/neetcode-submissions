class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMatrix = defaultdict(list)
        for src, dst in prerequisites:
            adjMatrix[src].append(dst)
        
        res = []
        visited = set()
        path = set()

        def dfs(i):
            if i in path:
                return False
            if i in visited:
                return True 
            
            path.add(i)
            for nbr in adjMatrix[i]:
                if not dfs(nbr):
                    return False
            res.append(i)
            visited.add(i)
            path.remove(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res
