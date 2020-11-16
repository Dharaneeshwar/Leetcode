# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,r1,r2):
        if(r1 is None and r2 is None):
            return True
        if(r1 is not None and r2 is not None):
            if r1.val==r2.val:
                return (self.check(r1.left,r2.right) and self.check(r1.right,r2.left))
        return False
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root,root)
        