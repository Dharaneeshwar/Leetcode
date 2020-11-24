# Time Complexity : O(n) ; 32 ms ; Inplace 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node, curr_node = None,None 
        curr_node = head
        while curr_node:
            next_node = curr_node.next 
            curr_node.next = prev_node # pointing next to previous
            prev_node = curr_node 
            curr_node = next_node 
        return prev_node    