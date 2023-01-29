class Node:
    def __init__(self, value, count, prev=None, next=None):
        self.value = value
        self.count = count
        self.prev = prev
        self.next = next
        self.cache_index = -1


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.item_count = 0
        self.head = None
        self.cache = [Node({-1: -1}, count=0) for i in range(capacity)]

    def get(self, key: int) -> int:

        node = self.findNode(key)
        if node == -1:
            return -1

        node.count += 1
        self.rePosition(node)

        return node.value[key]


    def put(self, key: int, value: int) -> None:

        node = self.findNode(key)

        # if node exists
        if node != -1:
            node.value[key] = value
            node.count += 1
            self.rePosition(node)

        # if not exists
        else:
            node = Node({key: value}, count=1)
            index = self.hashFunc(key)

            # if cache is not full
            if self.item_count != self.capacity:

                # if the position is occupied
                if list(self.cache[index].value.keys())[0] != -1:
                    while list(self.cache[index].value.keys())[0] != -1:
                        index = (index+1)%self.capacity

                self.cache[index] = node
                node.cache_index = index

                if self.item_count != 0:
                    node.next = self.cache[self.head].cache_index
                    self.cache[self.head].prev = index

                self.head = index

                self.item_count += 1

            # if cache is full
            else:
                node.next = self.cache[self.head].next
                self.cache[self.head] = node
                node.cache_index = self.head

    def printList(self) -> None:
        temp = self.cache[self.head]
        while temp.next is not None:
            print(f'value: {temp.value} - count: {temp.count}')
            temp = self.cache[temp.next]

        print(f'value: {temp.value} - count: {temp.count}')


    def rePosition(self, node: Node) -> None:

        if node.next is None:
            return
        search_node = self.cache[node.next]
        isHead = (node.cache_index == self.head)
        while search_node.next is not None:
            if node.count < search_node.count:
                if not isHead:
                    self.cache[node.prev].next = self.cache[node.next].cache_index
                    self.cache[node.next].prev = self.cache[node.prev].cache_index

                    node.next = search_node.cache_index
                    node.prev = search_node.prev

                    self.cache[search_node.prev].next = node.cache_index
                    search_node.prev = node.cache_index
                    break

            else:
                if isHead:
                    isHead = False
                    self.head = self.cache[node.next].cache_index
                    self.cache[self.head].prev = None

            search_node = self.cache[search_node.next]

        else:
            if not isHead:
                self.cache[node.prev].next = self.cache[node.next].cache_index
                self.cache[node.next].prev = self.cache[node.prev].cache_index
                node.prev = search_node.cache_index
                node.next = None



    def hashFunc(self, key: int) -> int:

        return key%self.capacity

    def findNode(self, key: int) -> Node:

        if self.item_count == 0:
            return -1

        index = self.hashFunc(key)
        if list(self.cache[index].value.keys())[0] != key:
            begin_index = index
            index = (index+1)%self.capacity
            while index != begin_index:
                if list(self.cache[index].value.keys())[0] == key:
                    return self.cache[index]

                index = (index + 1) % self.capacity

            return -1

        return self.cache[index]

cache = LFUCache(2)
cache.put(1,1)
print('===============')
cache.printList()
print('===============')
cache.put(2,2)
print('===============')
cache.printList()
print('===============')
print(cache.get(1))
cache.printList()
print('==============')
cache.put(3,3)
cache.printList()
print('================')
print(cache.get(2))
cache.printList()
print('===============')
print('===============')
print(cache.get(3))
cache.printList()
print('===============')
print('==============')
cache.put(4,4)
cache.printList()
print('================')
print(cache.get(1))
cache.printList()
print('===============')
print('==============')
print(cache.get(3))
cache.printList()
print('===============')
print('==============')
print(cache.get(4))
print('==============')
cache.printList()
print('===============')



