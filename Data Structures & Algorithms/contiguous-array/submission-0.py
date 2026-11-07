class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = {0: -1}
        last = balance = 0
        for i,n in enumerate(nums):
            balance += 1 if n else -1
            if balance in first:
                last = max(last, i-first[balance])
            else:
                first[balance] = i
        return last