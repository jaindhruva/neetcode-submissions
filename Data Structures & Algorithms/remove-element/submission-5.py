class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r :
            while l<=r and nums[l] != val:
                l += 1
            while l<=r and nums[r] == val:
                r -= 1
            if l<r:
                nums[l] = nums[r]
                r -= 1
            else:
                break
        return l
            