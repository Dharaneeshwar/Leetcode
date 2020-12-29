from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findpath(self,node,freq):
        if not node.left and not node.right:
            count = 0
            freq[node.val] += 1
            for value in freq:
                if freq[value]%2 == 1:
                    count += 1
            if count in [1,0]:
                self.noofpaths += 1 
            freq[node.val] -= 1    
            return
        freq[node.val] += 1
        if node.left:
            self.findpath(node.left,freq)
        if node.right:    
            self.findpath(node.right,freq)
        freq[node.val] -= 1

    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.noofpaths = 0
        self.findpath(root,defaultdict(int))
        return self.noofpaths