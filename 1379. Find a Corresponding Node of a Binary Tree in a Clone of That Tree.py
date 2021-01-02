# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.output = TreeNode() 
        
        def traverse(a,b,target):
            if not a or not b:
                return
            if a==target:
                self.output = b 
            traverse(a.left,b.left,target)
            traverse(a.right,b.right,target)    
            
    
        traverse(original,cloned,target)
        
        return self.output