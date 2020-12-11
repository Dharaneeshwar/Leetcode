# Recursive ; 20 ms ; faster than 99.05 %

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            temp = root.left 
            root.left = root.right 
            root.right = temp 
            # root.left, root.right =  root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            
        return root