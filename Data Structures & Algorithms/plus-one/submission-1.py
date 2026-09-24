class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        res = [0]*(n+1)
        for i in range(n-1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
            res[i+1] = digits[i]
        if carry == 1:
            res[0] = 1
            return res
        else:
            return res[1:]
            
            