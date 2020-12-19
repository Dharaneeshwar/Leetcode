# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,node):
        if not node:
            return
        if node.left:
            self.helper(node.left)
        self.l.append(node.val)
        if node.right:
            self.helper(node.right)
            
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.l = []
        self.helper(root)
        return self.l