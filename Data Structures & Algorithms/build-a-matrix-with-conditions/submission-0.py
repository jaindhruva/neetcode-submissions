class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def dfs(src, adj, visited, path, order):
            if src in path:
                return False
            if src in visited:
                return True
            
            visited.add(src)
            path.add(src)

            for nbr in adj[src]:
                if not dfs(nbr, adj, visited, path, order):
                    return False
            path.remove(src)
            order.append(src)
            return True

        def topo_sort(edges):
            adj = defaultdict(list)

            for src,dst in edges:
                adj[src].append(dst)
            
            visited, path = set(), set()
            order = []
            for src in range(1,k+1):
                if not dfs(src, adj, visited, path, order):
                    return []
            
            return order[::-1] # reverse]

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []

        index_map_row = {n:i for i,n in enumerate(row_order)}
        index_map_col = {n:i for i,n in enumerate(col_order)}

        res = [[0]*k for _ in range(k)]
        for num in range(1, k+1):
            r = index_map_row[num]
            c = index_map_col[num]
            res[r][c] = num

        return res