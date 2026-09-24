class Solution:
    def isHappy(self, n: int) -> bool:
        
        num_set = set()
        while True:
            sum = 0
            while n:
                remainder = n % 10
                sum = sum + (remainder)*(remainder)
                n = n//10
            if sum in num_set:
                return False
            if sum == 1:
                return True
            n = sum
            num_set.add(n)
        
        