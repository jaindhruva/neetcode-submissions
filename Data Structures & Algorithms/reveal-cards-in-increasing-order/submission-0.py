class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        res = [0]*n
        q = deque(range(n))

        for num in deck:
            i = q.popleft()
            res[i] = num
            if q:
                q.append(q.popleft())
        
        return res
