# 40 ms ; faster than 97.67 %

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
        if not root:
            return root 
        ret = root
        out = [[]]
        q = deque() 
        q.append(root)
        q.append(None)
        
        while len(q):
            temp = q.popleft()
            out[-1].append(temp)
            
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            
            if q[0] == None:
                q.popleft() 
                if len(q):
                    start = out[-1][0] 
                    for node in out[-1][1:]:
                        start.next = node 
                        start = node
                    out.append([])
                    q.append(None)

        start = out[-1][0] 
        for node in out[-1][1:]:
            start.next = node 
            start = node            
        return ret 