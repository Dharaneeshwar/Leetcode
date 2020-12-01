# push favouring implementation ; 28 ms 
# push - O(1)
# pop  - O(n)
 
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque() 
        self.q2 = deque() 

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """  
        if self.empty(): 
            return -1  
        else: 
            while len(self.q1)>1: 
                self.q2.append(self.q1.popleft()) 
        val = self.q1.popleft() 
        self.swap()
        return val
        
    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.q1) > 0: 
            return self.q1[-1]
        
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.q1)+len(self.q2) == 0: 
            return True 
        return False

    def swap(self):  # my function
        temp = self.q1 
        self.q1 = self.q2 
        self.q2 = temp 

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# TODO pop favouring  