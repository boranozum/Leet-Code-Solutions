class MyCircularQueue:

    def __init__(self, k: int):
        self.count = 0
        self.queue = [0 for i in range(k)]
        self.head = 0
        self.tail = k-1
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.tail = (self.tail+1)%self.size
        self.queue[self.tail] = value
        self.count += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = (self.head+1)%self.size
        self.count -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

myCircularQueue = MyCircularQueue(3)
myCircularQueue.enQueue(1)
myCircularQueue.enQueue(2)
myCircularQueue.enQueue(3)
myCircularQueue.enQueue(4)
myCircularQueue.Rear()
myCircularQueue.isFull()
myCircularQueue.deQueue()
myCircularQueue.enQueue(4)
myCircularQueue.Rear()