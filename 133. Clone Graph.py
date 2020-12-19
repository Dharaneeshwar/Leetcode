"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    dairy = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None 
        if node in self.dairy:
            return self.dairy[node]
        newnode = Node(node.val)

        self.dairy[node] = newnode 
        
        for n in node.neighbors:
            newnode.neighbors.append(self.cloneGraph(n))
            
        return newnode    