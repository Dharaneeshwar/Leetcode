# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        queue.append(None)
        l = [[]]
        
        while queue:
            temp = queue.popleft() 
            l[-1].append(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            if queue[0] == None:
                queue.popleft() 
                if len(queue):
                    if len(l)%2 == 0:
                        l[-1] = l[-1][::-1]    
                    l.append([])
                    queue.append(None)
        if len(l)%2 == 0:
            l[-1] = l[-1][::-1]                
        return l