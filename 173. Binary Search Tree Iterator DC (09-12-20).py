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