class MyQueue:
    
    def __init__(self):
        self.firstStack = []
        self.secondStack = []

    def push(self, x: int) -> None:
        self.firstStack.append(x)
        return
        

    def pop(self) -> int:
        for i in range(len(self.firstStack) - 1):
            self.secondStack.append(self.firstStack.pop())
        Ele = self.firstStack.pop()
        for i in range(len(self.secondStack)):
            self.firstStack.append(self.secondStack.pop())
        return Ele
            
        

    def peek(self) -> int:
        return self.firstStack[0]
        

    def empty(self) -> bool:
        return self.firstStack == []
