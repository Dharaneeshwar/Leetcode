class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [] 
        pushed = list(reversed(pushed))
        popped = list(reversed(popped))        
        while pushed:
            stack.append(pushed.pop())
            while stack and stack[-1] == popped[-1]:
                popped.pop() 
                stack.pop() 
        if not stack and not popped:
            return True 
        return False