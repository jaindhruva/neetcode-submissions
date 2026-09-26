class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        canReachFrom = [False]*n
        canReachFrom[n-1] = True
        start = n-2
        
        while start >= 0:
            window = nums[start]
            for j in range(start,min(n, start+window+1)):
                if canReachFrom[j] :
                    canReachFrom[start] = True
                    break
            start -= 1
        

        return canReachFrom[0]