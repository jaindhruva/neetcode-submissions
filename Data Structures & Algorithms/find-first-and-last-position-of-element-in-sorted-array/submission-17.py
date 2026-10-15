class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binarySearch(target):
            l, r = 0, len(nums)

            while l<r:
                mid = l + (r - l)//2
                
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid 
            return l
        res = [-1, -1]

        start = binarySearch(target)
        end = binarySearch(target+1) - 1

        if (not nums or
         start < 0 or start >= len(nums) or 
         end < 0 or end >= len(nums) or
         nums[start]!=target or nums[end]!=target) :
            return res
        

        return [start, end]
        