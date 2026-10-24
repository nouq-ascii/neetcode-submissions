class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.length = -1

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minStack == []:
            self.minStack.append(val)
        else:
            m = min(val, self.minStack[self.length])
            self.minStack.append(m)
        
        self.length += 1

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.length -= 1

    def top(self) -> int:
        return self.stack[self.length]

    def getMin(self) -> int:
        return self.minStack[self.length]
        
