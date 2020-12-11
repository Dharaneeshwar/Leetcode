# Recursive ; 220 ms ; faster than 98.15 % 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self,node,maximum):
        if node:
            if node.val >= maximum:
                self.count += 1
                maximum = node.val
            self.helper(node.left,maximum)    
            self.helper(node.right,maximum)    
            
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.helper(root,root.val)
        return self.count