# Not Efficient Spacewise (uses 2 deque) ; O(n) solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [] 
        q = deque() 
        out = deque()
        out.append([])
        q.append(root)
        q.append(None)
        
        while len(q):
            temp = q.popleft() 
            out[0].append(temp.val)
            
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            
            if q[0]==None:
                q.popleft()
                if len(q):
                    out.appendleft([])
                    q.append(None)
        return out                    