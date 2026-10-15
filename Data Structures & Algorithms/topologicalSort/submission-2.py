class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # create adj matrix
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        visited = set()
        path = set()  # for cycles
        res = []

        def dfs(node, visited, path, res):
            if node in path:
                return False

            if node in visited:
                return True
            path.add(node)

            for nbr in adj[node]:
                if not dfs(nbr, visited, path, res):
                    return False

            visited.add(node)
            res.append(node)
            path.remove(node)
            return True

        for i in range(n):
            if not dfs(i, visited, path, res):
                return []

        return res[::-1]
