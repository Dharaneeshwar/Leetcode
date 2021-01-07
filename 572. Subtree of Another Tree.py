# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def same(self,s,t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        return s.val == t.val and self.same(s.left,t.left) and self.same(s.right,t.right)
    
    def traverse(self,s,t):
        if self.treefound or not s:
            return 
        if s.val == t.val:
            if self.same(s,t):
                self.treefound = True
                return 
        self.traverse(s.left,t)
        self.traverse(s.right,t)
            
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        self.treefound = False
        self.traverse(s,t)
        return self.treefound