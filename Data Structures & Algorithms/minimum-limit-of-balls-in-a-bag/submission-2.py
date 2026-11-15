from math import ceil

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low, high = 1, max(nums)

        while low <= high:
            mid = low + (high - low)//2

            operations = 0
            for n in nums:
                operations += ceil(n / mid) - 1
            
            if operations <= maxOperations:
                high = mid - 1
            else:
                low = mid + 1
        
        return low