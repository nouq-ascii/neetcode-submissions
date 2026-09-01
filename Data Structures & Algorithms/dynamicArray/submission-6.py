class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.getSize():
            self.resize()
        self.arr[self.getSize()] = n

    def popback(self) -> int:
        num = self.arr[self.getSize()-1]
        self.arr[self.getSize()-1] = None
        return num 

    def resize(self) -> None:
        self.capacity *= 2
        arr2 = [None] * self.capacity
        for i in range(self.getSize()):
            arr2[i] = self.arr[i]
        self.arr = arr2

    def getSize(self) -> int:
        return len(self.arr) - (self.arr).count(None)
    
    def getCapacity(self) -> int:
        return self.capacity
