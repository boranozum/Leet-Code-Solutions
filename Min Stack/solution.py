class MinStack:

    def __init__(self):

        self.minElement = []
        self.stack = []
        self.itemCount = 0

    def push(self, val: int) -> None:

        self.stack.append(val)
        if len(self.minElement) == 0 or val <= self.minElement[-1]:
            self.minElement.append(val)

        self.itemCount += 1

    def pop(self) -> None:
        item = self.stack[-1]
        self.stack = self.stack[:-1]

        if item == self.minElement[-1]:
            self.minElement = self.minElement[:-1]

        self.itemCount -= 1

    def top(self) -> int:
        if self.itemCount == 0:
            return -1

        return self.stack[-1]


    def getMin(self) -> int:
        return self.minElement[-1]
