class HitCounter:

    def __init__(self):
        self.hitQueue = deque()

    def hit(self, timestamp: int) -> None:
        while self.hitQueue and self.hitQueue[0] <= timestamp-300:
            self.hitQueue.popleft()
        self.hitQueue.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.hitQueue and self.hitQueue[0] <= timestamp-300:
            self.hitQueue.popleft()
        return len(self.hitQueue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
