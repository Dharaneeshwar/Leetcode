# O(2n) ; faster than 98.17 %
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return [] 
        out = [[]]
        q = deque() 
        q.append(root)
        q.append(None)
        
        while len(q):
            temp = q.popleft()
            out[-1].append(temp.val)
            
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            
            if q[0] == None:
                q.popleft() 
                if len(q):
                    out[-1] = sum(out[-1])/len(out[-1])
                    out.append([])
                    q.append(None)
        out[-1] = sum(out[-1])/len(out[-1])        
        return out 