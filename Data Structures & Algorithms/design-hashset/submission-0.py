class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for _ in range(10000)]

    def add(self, key: int) -> None:
        slot = self.set[key % len(self.set)]
        while slot.next:
            if slot.next.key == key:
                return
            slot = slot.next
        slot.next = ListNode(key)

    def remove(self, key: int) -> None:
        slot = self.set[key % len(self.set)]
        while slot.next:
            if slot.next.key == key:
                slot.next = slot.next.next
                return
            slot = slot.next

    def contains(self, key: int) -> bool:
        slot = self.set[key % len(self.set)]
        while slot.next:
            if slot.next.key == key:
                return True
            slot = slot.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)