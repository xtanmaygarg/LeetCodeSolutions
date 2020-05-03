class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [1e20]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minStack[-1] >= x:
            self.minStack.append(x)
        return

    def pop(self) -> None:
        Num = self.stack.pop()
        if Num == self.minStack[-1]:
            self.minStack.pop()
        return

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
