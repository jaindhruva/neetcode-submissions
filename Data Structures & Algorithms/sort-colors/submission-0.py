class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        index = 0
        for colour in range(3):
            for i in range(count[colour]):
                nums[index] = colour
                index += 1
        
        