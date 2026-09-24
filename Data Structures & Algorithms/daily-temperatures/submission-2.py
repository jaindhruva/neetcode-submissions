class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = []
        for i in range(n):
            rev_i = n-i-1
            temp = temperatures[rev_i]
            while len(stack)>0 and stack[-1][0] <= temp:
                stack.pop()
            if len(stack)==0:
                stack.append([temp, i])
                res.append(0)
                continue
            if stack[-1][0] > temp:
                res.append(i - stack[-1][1])
                stack.append([temp, i])
                continue
        res.reverse()
        return res
            