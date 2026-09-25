class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {} # key -> Node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._add(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        curr = self.head

        self.cache[key] = Node(key, value)
        self._add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

    def _remove(self, node: Node) -> None:
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def _add(self, node: None) -> None:
        prev, next = self.tail.prev, self.tail
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

class Node:
    def __init__(self, key: int, val: int, prev: Node | None = None, next: Node | None = None):
        self.key, self.val = key, val
        self.prev, self.next = prev, next
        
        
