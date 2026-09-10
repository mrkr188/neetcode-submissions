class MyStack:

    def __init__(self):
        self.queue = None

    def push(self, x: int) -> None:
        # pushing 1, 2, then 3 creates: deque([3, deque([2, deque([1, None])])])
        # this is kind of like linked list which holds next queue
        self.queue = deque([x, self.queue])

    def pop(self) -> int:
        print(self.queue)
        top = self.queue.popleft()
        self.queue = self.queue.popleft()
        return top

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return self.queue == None
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()