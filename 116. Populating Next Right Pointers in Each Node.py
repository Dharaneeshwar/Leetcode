# 60 ms ; faster than 75.64 %
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        q = deque() 
        q.append(root)
        q.append(None)
        l = [[]]
        while len(q):
            temp = q.popleft()
            l[-1].append(temp)  
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            
            if q[0] == None:
                q.popleft() 
                if len(q):
                    node = l[-1][0]
                    for i in range(1,len(l[-1])):
                        node.next = l[-1][i] 
                        node = node.next
                    l.append([])
                    q.append(None)
        node = l[-1][0]
        for i in range(1,len(l[-1])):
            node.next = l[-1][i] 
            node = node.next            
        return root