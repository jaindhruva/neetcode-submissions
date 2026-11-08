class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum = 0
        countMap = {}
        sum = 0

        for i in range(k):
            n = nums[i]
            sum += n
            countMap[n] = countMap.get(n, 0) + 1

        if len(countMap) == k:
            maxSum = sum
            
        for i in range(1, len(nums) - k + 1):
            l = nums[i - 1]
            r = nums[i + k - 1]
            countMap[r] = countMap.get(r, 0) + 1
            
            countMap[l] -= 1
            if countMap[l] == 0:
                countMap.pop(l)
            sum = sum + r - l

            if len(countMap) == k:
                maxSum = max(maxSum, sum)

        return maxSum

