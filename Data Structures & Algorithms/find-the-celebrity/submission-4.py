# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # knowNoone = set() 
        candidate = 0

        # this will leave you with 1 , since you iterate n times,
        # and each timeyou eleminate one
        for i in range(n):
            if knows(candidate, i):
                candidate = i
        
        # if anyone doesnt know him, he is not celeb
        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate, i) or not knows(i, candidate):
                return -1
        

        return candidate

            