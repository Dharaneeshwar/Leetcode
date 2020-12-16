# O(2n) ; inorder - O(n) ; check - O(n-1) ;

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def in_helper(self,root):
        if not root:
            return 
        self.in_helper(root.left)
        self.inorder.append(root.val)
        self.in_helper(root.right)
    
    def check(self):
        for i in range(1,len(self.inorder)):
            if self.inorder[i] <= self.inorder[i-1]:
                return False 
        return True    
    
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return
        self.inorder = [] 
        self.in_helper(root)
        if self.check():
            return True
        return False