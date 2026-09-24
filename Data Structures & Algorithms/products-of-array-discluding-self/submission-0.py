class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_to_right , right_to_left = [0]*n, [0]*n

        left_to_right[0] = nums[0]
        for i in range (1,n):
            left_to_right[i] = nums[i]*left_to_right[i-1]
        
        right_to_left[n-1] = nums[n-1]
        for i in range (1,n):
            j = n-1-i
            right_to_left[j] = nums[j]*right_to_left[j+1]
        
        res = [0]*n
        res[0] = right_to_left[1]
        res[n-1] = left_to_right[n-2]
        for i in range(1,n-1):
            res[i] = left_to_right[i-1]*right_to_left[i+1]
        
        return res
