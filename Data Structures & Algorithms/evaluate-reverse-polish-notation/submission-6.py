class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            # print(stack)
            if t == '+':
                num = stack.pop() + stack.pop()
                stack.append(num)
            elif t == '-':
                num = -1*stack.pop() + stack.pop()
                stack.append(num)
            elif t == '*':
                num = stack.pop() * stack.pop()
                stack.append(num)
            elif t == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                num = n2 / n1
                stack.append(int(num))
                print(stack[-1])
            else:
                stack.append(int(t)-int('0'))
            

        return stack.pop()
