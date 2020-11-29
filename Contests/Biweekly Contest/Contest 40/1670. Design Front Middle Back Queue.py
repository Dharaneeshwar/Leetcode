class FrontMiddleBackQueue:
    l = []
    def __init__(self):
        self.l = []

    def pushFront(self, val: int) -> None:
        print(self.l)
        self.l = [val]+self.l
        print(self.l)

    def pushMiddle(self, val: int) -> None:
        le = len(self.l)
        self.l.insert(le//2,val)

    def pushBack(self, val: int) -> None:
        self.l = self.l + [val] 
       
    def popFront(self) -> int:
        try:
            val = self.l[0]
            self.l = self.l[1:] 
            return val
        except:
            return -1

    def popMiddle(self) -> int:
        le = len(self.l)
        if le==0:
            return -1
        if le%2==0:
            mid = le//2-1
        else:
            mid = le//2
        val = self.l[mid]
        self.l = self.l[:mid] + self.l[mid+1:]
        return val
    
    def popBack(self) -> int:
        try:
            val = self.l[-1]
            self.l = self.l[:-1]
            return val
        except:
            return -1

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

# TODO Using linked list