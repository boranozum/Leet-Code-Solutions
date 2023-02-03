class FrontMiddleBackQueue:

    def __init__(self):

        self.queue = []
        self.item_count = 0

    def pushFront(self, val: int) -> None:

        self.queue = [val] + self.queue
        self.item_count += 1

    def pushMiddle(self, val: int) -> None:

        middle = int(self.item_count/2)
        self.queue = self.queue[:middle] + [val] + self.queue[middle:]
        self.item_count += 1


    def pushBack(self, val: int) -> None:

        self.queue.append(val)
        self.item_count += 1

    def popFront(self) -> int:

        if self.item_count == 0:
            return -1

        val = self.queue[0]
        self.queue = self.queue[1:]
        self.item_count -= 1

        return val

    def popMiddle(self) -> int:
        val = 0
        if self.item_count == 0:
            return -1

        if self.item_count % 2 == 0:
            middle = int(self.item_count/2)
            val = self.queue[middle-1]
            self.queue = self.queue[:middle-1] + self.queue[middle:]

        else:
            middle = int(self.item_count/2)
            val = self.queue[middle]
            self.queue = self.queue[:middle] + self.queue[middle+1:]

        self.item_count -= 1

        return val


    def popBack(self) -> int:
        if self.item_count == 0:
            return -1

        val = self.queue[-1]
        self.queue = self.queue[:-1]
        self.item_count -= 1

        return val
