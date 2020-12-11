# Time Complexity - O(2n) ; 76 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def createarr(self,root):
        if not root: 
            return 
        self.createarr(root.left)
        self.arr += [root.val]
        self.createarr(root.right)
        
    def __init__(self, root: TreeNode):
        self.arr = []
        self.ind = 0
        self.createarr(root)
        self.leng = len(self.arr)
        
    def next(self) -> int:
        self.ind+=1
        return self.arr[self.ind-1]         

    def hasNext(self) -> bool:
        if self.ind < self.leng:
            return True 
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Time Complexity - O(n) ; 68 ms ; faster than 91.69 %

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop() 
        req_value = node.val 
        # go right if possible 
        if node.right:
            node = node.right
            # now moving left from the right node
            while node:
                self.stack.append(node)
                node = node.left 
        return req_value        

    def hasNext(self) -> bool:
        if self.stack:
            return True 
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()