class Logger:

    def __init__(self):
        self.q = deque()
        self.messageTsMap = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messageTsMap:
            self.messageTsMap[message] = timestamp
            self.q.append(message)
        else:
            if timestamp < self.messageTsMap[message] + 10:
                return False
            else:
                self.messageTsMap[message] = timestamp
                while self.q[0] != message:
                    msg = self.q.popleft()
                    self.messageTsMap.remove(msg)
                msg = self.q.popleft()
                self.q.append(message)
                return True
        if len(self.q) > 10:
            msg = self.q.popleft()
            self.messageTsMap.remove(msg)
        
        return True
        

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
