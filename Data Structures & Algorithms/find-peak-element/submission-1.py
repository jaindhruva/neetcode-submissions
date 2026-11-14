class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1

        while l<r:
            m = l + (r-l)//2
            if nums[m] > nums[m+1] :
                r = m
            else:
                l = m+1
        return l
