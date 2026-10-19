class Solution:
    def totalMoney(self, n: int) -> int:
        quotient = n//7
        q_sum = quotient*28 + 7*quotient*(quotient-1)//2

        remainder = n%7
        r_sum = 0
        i = 0
        r_sum = remainder*(quotient+1) + remainder*(remainder-1)//2
        return q_sum + r_sum
