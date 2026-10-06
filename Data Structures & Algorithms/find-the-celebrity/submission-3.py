# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        knowNoone = set() 

        for i in range(n):
            knowNoone.add(i)
            for j in range(n):
                if i == j:
                    continue
                if knows(i,j):
                    knowNoone.remove(i)
                    break
        
        for j in list(knowNoone):
            isACeleb = True
            for i in range(n):
                if not knows(i,j):
                    isACeleb = False
                    break
            if isACeleb:
                return j
        

        return -1

            