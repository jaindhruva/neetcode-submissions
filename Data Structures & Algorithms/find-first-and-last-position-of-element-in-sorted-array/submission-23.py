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

        start = binarySearch(target)
        end = binarySearch(target+1) - 1

        if ( start >= len(nums) or nums[start]!=target ) :
            return [-1, -1]

        return [start, end]
        