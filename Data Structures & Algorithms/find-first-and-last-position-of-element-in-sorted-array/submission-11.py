class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, mid, r = 0, 0, len(nums)
        res = [-1,-1]
        if not nums:
            return res

        while l<=r:
            mid = (l + r )//2
            
            if mid >= len(nums) or nums[mid] == target:
                break
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        if mid >= len(nums) or nums[mid] != target:
            return res
        
        l, r = mid, mid

        while l>=0 and nums[l] == target:
            l -= 1
        res[0] = l + 1

        while r<len(nums) and nums[r] == target:
            r += 1
        res[1] = r - 1

        return res
        