# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse_helper(self,node,to_delete):
        if not node:
            return None
        
        node.left = self.traverse_helper(node.left,to_delete) 
        node.right = self.traverse_helper(node.right,to_delete)
        
        if node.val in to_delete:
            if node.left:
                self.nodes.append(node.left)
            if node.right:
                self.nodes.append(node.right)
            return None     
        return node
        
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.nodes = []
        if not root:
            return []
        to_delete = set(to_delete)
        self.traverse_helper(root,to_delete)
        if root.val not in to_delete:
            self.nodes.append(root)
        return self.nodes    