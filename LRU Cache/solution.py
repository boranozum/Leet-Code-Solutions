class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.linkedList = []
        self.count = 0
        self.capacity = capacity

        self.head = None
        self.tail = None

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def get(self, key: int) -> int:

        if self.count == 0:
            return -1

        search_node = self.head
        while list(search_node.value.keys())[0] != key:
            search_node = search_node.next
            if search_node is None:
                return -1

        if search_node.prev is None and search_node.next is not None:
            search_node.next.prev=None
            self.head = search_node.next

        elif search_node.prev is not None and search_node.next is not None:
            search_node.prev.next = search_node.next
            search_node.next.prev = search_node.prev

        search_node.prev = self.tail
        self.tail.next = search_node
        search_node.next = None
        self.tail = search_node

        return search_node.value[key]

    def put(self, key: int, value: int) -> None:

        node = self.getNode(key)
        if node is not None:
            node.value[key] = value
            return

        node = Node({key: value})

        if self.count == self.capacity:
            if self.capacity == 1:
                self.head = node
                self.tail = node
            else:
                self.head = self.head.next
                self.head.prev = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = node

        elif self.count == 0:
            self.head = node
            self.tail = node
            self.count += 1

        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.count += 1

    def getNode(self, key: int) -> Node:

        if self.count == 0:
            return None

        search_node = self.head
        while list(search_node.value.keys())[0] != key:
            search_node = search_node.next
            if search_node is None:
                return None

        if search_node.prev is None and search_node.next is not None:
            search_node.next.prev=None
            self.head = search_node.next

        elif search_node.prev is not None and search_node.next is not None:
            search_node.prev.next = search_node.next
            search_node.next.prev = search_node.prev

        search_node.prev = self.tail
        self.tail.next = search_node
        search_node.next = None
        self.tail = search_node

        return search_node



lru = LRUCache(2)
lru.put(1,1)
lru.printList()
print("=========")
lru.put(2,2)
lru.printList()
print("=========")
print(lru.get(1))
lru.printList()
print("=========")
lru.put(3,3)
lru.printList()
print("=========")
print(lru.get(2))
lru.printList()
print("=========")
lru.put(4,4)
lru.printList()
print("=========")
print("=========")
print(lru.get(1))
lru.printList()
print("=========")
print(lru.get(3))
lru.printList()
print("=========")
print(lru.get(4))
lru.printList()
print("=========")

