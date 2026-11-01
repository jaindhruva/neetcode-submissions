class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        if total == 0:
            return 0

        currSum = 0
        for i,n in enumerate(nums):

            if (total-n)%2 == 0 and  currSum == (total - n) // 2:
                return i
            currSum += n

        return -1