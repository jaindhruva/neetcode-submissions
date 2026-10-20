class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        increasing = False
        decreasing = False
        for i in range(2,len(nums)):
            if nums[i] == nums[i-1] and nums[i-1] == nums[i-2] :
                continue
            if nums[i] >= nums[i-1] and nums[i-1] >= nums[i-2] :
                increasing = True
                if decreasing:
                    return False
                continue
            if nums[i] <= nums[i-1] and nums[i-1] <= nums[i-2] :
                decreasing = True
                if increasing:
                    return False
                continue
            return False
        
        return True
            