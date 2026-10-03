class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjMatrix = defaultdict(list)
        for i in range(len(edges)):
            v1,v2 = edges[i]
            prob = succProb[i]
            adjMatrix[v1].append([v2,prob])
            adjMatrix[v2].append([v1,prob])
        
        maxHeap = []
        resProb = 1
        currNode = start_node
        visited = set()

        heapq.heappush(maxHeap, (-resProb, currNode))

        while maxHeap:
            # print(maxHeap)
            resProb, node = heapq.heappop(maxHeap)
            visited.add(node)
            # print(resProb, node)
            if node == end_node:
                return -resProb

            for nbr,nbrProb in adjMatrix[node]:
                if nbr not in visited:
                    heapq.heappush(maxHeap, (-abs(resProb*nbrProb),nbr))
        
        return 0