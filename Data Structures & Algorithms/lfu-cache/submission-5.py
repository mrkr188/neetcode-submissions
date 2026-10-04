class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        # sentinel head and tail nodes for easy O(1) insertions and deletions
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def length(self):
        return self.size

    def push(self, node):
        # insert node right before the tail (most recently used in this frequency bucket)
        left = self.tail.prev
        left.next = node
        node.prev = left
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    def pop(self, node):
        # remove an arbitrary node from the doubly linked list
        left, right = node.prev, node.next
        left.next = right
        right.prev = left
        # node.prev = None
        # node.next = None
        self.size -= 1

    def popleft(self):
        # remove and return the least recently used node in this frequency bucket (right after head)
        if self.length() == 0:
            return None
        node = self.head.next
        self.pop(node)
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0  # tracks the current minimum frequency in the cache
        self.nodeMap = {}  # maps key -> ListNode
        # maps frequency -> LinkedList of nodes with that frequency
        self.listMap = defaultdict(LinkedList)

    # update node's frequency when accessed (get or put)
    def counter(self, node):
        cnt = node.freq
        self.listMap[cnt].pop(node)

        # if the LFU bucket is now empty, increment lfuCnt to the next frequency
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1

        node.freq += 1
        self.listMap[node.freq].push(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.counter(node)  # access increments frequency
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        # if key already exists, update its value and frequency
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.counter(node)
            return

        # if capacity is reached, evict the least frequently used (and oldest) item
        if len(self.nodeMap) == self.cap:
            node = self.listMap[self.lfuCnt].popleft()
            self.nodeMap.pop(node.key)

        # insert the new node with frequency 1
        node = ListNode(key, value)
        self.nodeMap[key] = node
        self.listMap[1].push(node)
        self.lfuCnt = 1  # reset minimum frequency to 1 for the new node


