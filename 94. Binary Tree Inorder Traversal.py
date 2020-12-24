# Recursive

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

# Iterative using stack 

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        l = [] 
     
        while True:
            while root:
                stack.append(root)
                root = root.left 
            if not stack:
                break
            temp = stack.pop()
            l.append(temp.val)
            root = temp.right 

        return l