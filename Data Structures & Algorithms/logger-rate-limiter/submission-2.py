class Logger:

    def __init__(self):
        self.q = deque()
        self.messageTsMap = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messageTsMap:
            self.messageTsMap[message] = timestamp
            return True
        if timestamp >= self.messageTsMap[message] + 10:
            self.messageTsMap[message] = timestamp
            return True
        
        
        return False
        

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
