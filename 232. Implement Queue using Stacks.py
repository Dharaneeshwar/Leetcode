# enqueue favouring logic ; 28 ms 
# enqueue - O(1)
# dequeue - O(n)

class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = [] 
        self.s2 = [] 
        
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """ 
        self.s1.append(x)
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
           return -1 
        else:
            if len(self.s2) > 0:
                val = self.s2.pop()
                return val 
            else:
                while len(self.s1) > 1:
                    self.s2.append(self.s1.pop())
                val = self.s1.pop() 
                return val

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return -1 
        else:
            if len(self.s2) > 0:
                return self.s2[-1] 
            else:
                return self.s1[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1)+len(self.s2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# TODO Dequeue Favouring