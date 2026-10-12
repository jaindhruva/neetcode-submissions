class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slowPtr = fastPtr = 0
        while True:
            slowPtr = nums[slowPtr]
            fastPtr = nums[nums[fastPtr]]
            if slowPtr == fastPtr:
                break
        
        slowPtr2 = 0
        while True:
            slowPtr = nums[slowPtr]
            slowPtr2 = nums[slowPtr2]
            if slowPtr == slowPtr2:
                break
        
        return slowPtr
