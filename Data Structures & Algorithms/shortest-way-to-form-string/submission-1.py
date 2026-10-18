class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i, count = 0, 0

        while i < len(target):
            j = 0
            found_match = False
            while j < len(source):
                if target[i] == source[j]:
                    i += 1
                    found_match = True
                    if i == len(target):
                        break
                j += 1
            count += 1
            if not found_match:
                return -1

        return count 
            
