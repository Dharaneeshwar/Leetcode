# Time Complexity : O(n) ; 16 ms ; faster than 99.84 %

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        prev_node = None 
        curr_node = head
        next_node = None 
        if m!=1:    
            start_node = head

            for i in range(m-2):
                start_node = start_node.next 
    
            curr_node = start_node.next            
            reverse_start = start_node.next            
        else:
            reverse_start = head
        for i in range(n-m+1):

            next_node = curr_node.next
            curr_node.next = prev_node 
            prev_node = curr_node 
            curr_node = next_node 
    
        if m==1:
            head = prev_node
        else:
            start_node.next = prev_node  
        
        reverse_start.next = curr_node 
            
        return head
