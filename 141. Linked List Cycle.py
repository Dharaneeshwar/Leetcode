# Hashing ; O(n) Space
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
    
# O(1) space ; Floyd's cycle

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        if head.next == None:
            return False
        slow ,fast = head, head.next 
        while slow and fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next 
            fast = fast.next.next
        return False    