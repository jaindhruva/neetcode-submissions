class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('infinity')
        l = 0
        subArrSum = 0
        for r in range(len(nums)):
            # if subArrSum < target:
            subArrSum += nums[r]
            while subArrSum >= target:
                minLen = min(minLen, r-l+1)
                subArrSum -= nums[l]
                l += 1


        return 0 if minLen == float('infinity') else minLen