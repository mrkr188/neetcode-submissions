class FreqStack:
    def __init__(self):
        # value: frequency count
        self.count = {}
        # frequency: stack of values at that frequency
        self.stack = {}
        # current highest frequency across all elements
        self.maxCount = 0

    def push(self, val: int) -> None:
        # increment frequency count for current value
        valCount = self.count.get(val, 0) + 1
        self.count[val] = valCount

        # update max frequency and push value into its frequency bucket
        if valCount > self.maxCount:
            self.maxCount = valCount
            self.stack[valCount] = [val]
        else:
            self.stack[valCount].append(val)

    def pop(self) -> int:
        # guard against popping from an empty stack
        if self.maxCount == 0:
            return -1

        # pop most recent value from highest frequency bucket
        res = self.stack[self.maxCount].pop()
        self.count[res] -= 1

        # decrement max frequency if top bucket becomes empty
        if len(self.stack[self.maxCount]) == 0:
            self.maxCount -= 1

        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()