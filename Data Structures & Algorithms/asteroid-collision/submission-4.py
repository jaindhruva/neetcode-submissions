class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        posStack = []
        res = []

        for a in asteroids:
            if len(posStack) == 0 and a<=0:
                res.append(a)
                continue
            if a > 0:
                posStack.append(a)
                continue
            else:
                if abs(a) == posStack[-1]:
                    posStack.pop()
                    continue
                while posStack and abs(a) > posStack[-1]:
                    posStack.pop()
                if not posStack:
                    res.append(a)
                    continue
                if abs(a) == posStack[-1]:
                    posStack.pop()
                
        res += posStack
        print(res)
        return res