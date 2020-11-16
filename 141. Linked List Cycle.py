class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        l=[]  
        node=head
        while node!=None: 
            if node not in l: 
                l.append(node) 
            else: 
                return True 
            node=node.next  
        return False
    