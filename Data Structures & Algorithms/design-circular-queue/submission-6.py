class LinkNode:

    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.size < self.capacity:
            node = LinkNode(value)
            if self.size == 0:
                self.head = node
                self.tail = node
                node.next = node
                node.prev = node
                self.size += 1
                return True
            temp = self.tail
            self.tail.next = node
            self.tail = node
            node.prev = temp
            node.next = self.head
            self.head.prev = node
            self.size += 1
            return True
        return False


    def deQueue(self) -> bool:
        if self.size == 1:
            self.size -= 1
            self.head = None
            self.tail = None
            return True
        if self.size>0:
            self.head = self.head.next
            if self.head:
                self.head.prev = self.tail
            self.tail.prev = self.head
            self.size -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        return self.head.val if self.head else -1

    def Rear(self) -> int:
        return self.tail.val if self.tail else -1

    def isEmpty(self) -> bool:
        return (self.size == 0)

    def isFull(self) -> bool:
        return (self.size == self.capacity) 
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()