class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        l, r = 0, k-1
        res = []
        countMap = Counter(nums[:k])
        for n in nums[:k]:
            heapq.heappush(minHeap, -n )
        res.append(-minHeap[0])
        while r < len(nums)-1:
            # print(minHeap)
            # print(countMap)
            countMap[nums[l]] -= 1
            # print(nums[l],countMap[-minHeap[0]])
            l += 1
            while minHeap and countMap[-minHeap[0]] == 0:
                heapq.heappop(minHeap)
            r += 1
            if nums[r] not in countMap:
                countMap[nums[r]] = 0
            countMap[nums[r]] += 1
            heapq.heappush(minHeap, -nums[r])
            res.append(-minHeap[0])

        return res
