# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None:
            return 1+self.minDepth(root.right)
        if root.right is None:
            return 1+self.minDepth(root.left)
        return min(1+self.minDepth(root.left),1+self.minDepth(root.right))