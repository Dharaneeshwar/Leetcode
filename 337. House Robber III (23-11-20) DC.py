# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(n):
            if not n:
                return (0,0)
            left = helper(n.left)
            right = helper(n.right)
            
            rob = n.val + left[1] + right[1] 
            
            notrob = max(left) + max(right) 
            
            return [rob,notrob]
        return max(helper(root))    