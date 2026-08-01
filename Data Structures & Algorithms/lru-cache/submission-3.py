class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.right = self.tail
        self.tail.left = self.head
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
            lru = self.head.right
            self._remove(lru)
            del self.cache[lru.key]

    def _remove(self, node: Node) -> None:
        left, right = node.left, node.right
        left.right = right
        right.left = left

    def _add(self, node: None) -> None:
        left, right = self.tail.left, self.tail
        left.right = node
        right.left = node
        node.right = right
        node.left = left

class Node:
    def __init__(self, key: int, val: int, left: Node | None = None, right: Node | None = None):
        self.key, self.val = key, val
        self.left, self.right = left, right
        
        
