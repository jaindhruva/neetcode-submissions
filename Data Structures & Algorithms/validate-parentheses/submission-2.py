class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c =='[' or c == '{':
                stack.append(c)
            elif c == ')' and stack and stack[-1] != '(':
                return False
            elif c == ']' and stack and stack[-1] != '[':
                return False
            elif c == '}' and stack and stack[-1] != '{':
                return False
            elif stack:
                stack.pop()
            else:
                return False
        return True if not stack else False
                