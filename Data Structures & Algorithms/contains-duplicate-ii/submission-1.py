class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(0, len(nums)):
            n1 = nums[i]
            for j in range (i+1, i+1+k):
                if j>=len(nums):
                    continue
                if n1 == nums[j]:
                    return True
        return False