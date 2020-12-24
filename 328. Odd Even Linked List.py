# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head    
        
        pivot = head 
        node = head.next
        while node and node.next:
            temp = node.next 
            node.next = temp.next 
            temp.next = pivot.next 
            pivot.next = temp 
            pivot = pivot.next 
            node = node.next
        return head