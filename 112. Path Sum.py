# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        print(sum)
        if root==None:
            return False 
        sum-=root.val 
        if (root.left==None and root.right==None and sum==0):
            return True 
        return Solution().hasPathSum(root.left,sum) or Solution().hasPathSum(root.right,sum)