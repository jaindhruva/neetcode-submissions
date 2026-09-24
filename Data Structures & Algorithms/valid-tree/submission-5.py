class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj_matrix = defaultdict(list)
        for node1, node2 in edges:
            adj_matrix[node1].append(node2)
            adj_matrix[node2].append(node1)
        
        visited = set()

        def dfs(node, par):
            if node in visited:
                return False

            visited.add(node)
            for nbr in adj_matrix[node]:
                if nbr == par:
                    continue
                if not dfs(nbr, node):
                    return False
            return True

        return dfs(0,-1) and len(visited)==n