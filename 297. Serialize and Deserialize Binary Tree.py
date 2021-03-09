# 104 ms ; faster than 95.59 %

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        string = []
        queue = deque() 
        queue.append(root)
        string.append(str(root.val))
        while len(queue):
            node = queue.popleft() 
            if node.left:
                string.append(str(node.left.val))
                queue.append(node.left)
            else:
                string.append(str("None")) 
            if node.right:
                string.append(str(node.right.val))
                queue.append(node.right)
            else:
                string.append(str("None")) 
        string = '_'.join(string)        
        string = string.rstrip('_None')        
        return string
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        if len(data) == 0:
            return
        if '_' in data:
            data = data.split('_')
            print(data)
        else:
            return TreeNode(int(data))

        nodes = [None if val == 'None' else TreeNode(int(val)) for val in data]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left  = kids.pop()
                if kids: node.right = kids.pop()
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))