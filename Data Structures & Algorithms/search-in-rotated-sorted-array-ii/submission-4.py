class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n-1

        while l <= r:
            m = l + (r-l)//2
            if target in (nums[l], nums[m], nums[r]):
                return True
            # find sorted side and check if target is there.
            if nums[l] < nums[m]:
                if nums[l] < target < nums[m]:
                    r = m-1                    
                else:
                    l = m+1
                continue
            if nums[m] < nums[r]:
                if nums[m] < target < nums[r]:
                    l = m+1
                else:
                    r = m-1
                continue
            l += 1




        
        return False
