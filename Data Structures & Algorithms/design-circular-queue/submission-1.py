class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.head = ListNode(0)
        # head and tail are same for empty queue
        self.tail = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        cur = ListNode(value)
        if self.isEmpty():
            self.head.next = cur
            self.tail = cur
        else:
            self.tail.next = cur
            self.tail = cur

        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False

        self.head.next = self.head.next.next
        # tail removed, update tail to head
        if self.head.next is None:
            self.tail = self.head

        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.head.next is None

    def isFull(self) -> bool:
        return self.space == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()