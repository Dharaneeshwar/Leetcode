# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        nodes = set()
        while head:
            if head in nodes:
                return head 
            else:
                nodes.add(head)
                head = head.next 
        return None        
            
# O(1) Space ; Fload Algo 

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if head.next == None:
            return None
        slow ,fast = head, head.next 
        while slow and fast and fast.next:
            if slow == fast:
                slow = slow.next 
                while slow != head:
                    slow = slow.next 
                    head = head.next 
                return head    
            slow = slow.next 
            fast = fast.next.next
        return None
        