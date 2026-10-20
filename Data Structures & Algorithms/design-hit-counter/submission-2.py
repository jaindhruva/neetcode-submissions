class HitCounter:

    def __init__(self):
        self.hitQueue = deque()

    def cleanup(self, timestamp):
        while self.hitQueue and self.hitQueue[0] <= timestamp-300:
            self.hitQueue.popleft()

    def hit(self, timestamp: int) -> None:
        self.cleanup(timestamp)
        self.hitQueue.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        self.cleanup(timestamp)
        return len(self.hitQueue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
