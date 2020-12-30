"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0 
        self.maxdepth = 0

        def depthfinder(node,depth):
            for child in node.children:
                depthfinder(child,depth+1)   
            self.maxdepth = max(self.maxdepth,depth)
            
        depthfinder(root,1)
        return self.maxdepth