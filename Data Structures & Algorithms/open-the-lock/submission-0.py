class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getNextPossibleCombinations(code):
            res = []
            for i in range(4):
                slot = int(code[i])
                prevSlot = str((slot-1+10)%10)
                res.append(code[:i] + prevSlot + code[(i+1):])
                nextSlot = str((slot+1)%10)
                res.append(code[:i] + nextSlot + code[(i+1):])
            return res

        if "0000" in deadends:
            return -1

        visited = set(deadends)
        q = deque()
        q.append('0000')
        moves = 0
        while q:
            
            for i in range(len(q)):
                code = q.popleft()
                if code == target:
                    return moves
                
                for nextCode in getNextPossibleCombinations(code):
                    if nextCode not in visited:
                        visited.add(nextCode)
                        q.append(nextCode)
            moves += 1
            
        
        return -1
            

