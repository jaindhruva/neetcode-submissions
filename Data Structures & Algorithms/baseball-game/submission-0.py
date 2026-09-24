class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for c in operations:
            
            if c == 'C':
                stack.pop()
                continue
            if c == '+':
                sum = int(stack[len(stack)-1]) + int(stack[len(stack)-2])
                stack.append(str(sum))
                continue
            if c == 'D':
                double = int(stack[len(stack)-1])*2 
                stack.append(str(double))
                continue
            stack.append(c)
        
        res = 0
        while len(stack) > 0:
            res += int(stack.pop())
        
        return res
            