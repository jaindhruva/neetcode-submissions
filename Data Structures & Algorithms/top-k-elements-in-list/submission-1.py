class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}

        for n in nums:
            count_map[n]= count_map.get(n,0)+1
        
        heap = []
        for num in count_map.keys():
            heapq.heappush(heap, (count_map[num],num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        