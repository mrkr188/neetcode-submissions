class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.store = [ListNode() for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        slot = self.store[key%10000]
        while slot.next:
            if key == slot.next.key:
                slot.next.value = value
                return
            slot = slot.next
        slot.next = ListNode(key, value)

    def get(self, key: int) -> int:
        slot = self.store[key%10000]
        while slot.next:
            if key == slot.next.key:
                return slot.next.value
            slot = slot.next
        return -1
        
    def remove(self, key: int) -> None:
        slot = self.store[key%10000]
        while slot.next:
            if key == slot.next.key:
                slot.next = slot.next.next
                return
            slot = slot.next        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)