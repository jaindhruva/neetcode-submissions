class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum = 0
        countMap = {}
        sum = 0

        for i in range(k):
            n = nums[i]
            sum += n
            if n not in countMap:
                countMap[n] = 0
            countMap[n] += 1

        if len(countMap) == k:
            maxSum = sum
            
        for i in range(1, len(nums) - k + 1):
            l = nums[i - 1]
            r = nums[i + k - 1]
            if r not in countMap:
                countMap[r] = 0
            countMap[r] += 1
            countMap[l] -= 1
            if countMap[l] == 0:
                countMap.pop(l)
            sum += r
            sum -= l

            if len(countMap) == k:
                maxSum = max(maxSum, sum)

        return maxSum

