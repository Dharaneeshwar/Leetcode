# Recursive Solution 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1 
        if l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2

#  Iterative Solution ; 24 ms ; faster than 99.56 %    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = None
        out = output 
        while l1 and l2:
            if l1.val <= l2.val:
                if out:
                    newnode = ListNode(l1.val)
                    out.next = newnode
                    out = out.next
                else:
                    out = ListNode(l1.val) 
                    output = out
                l1 = l1.next    
            else:
                if out:
                    newnode = ListNode(l2.val)
                    out.next = newnode 
                    out = out.next
                else:
                    out = ListNode(l2.val)
                    output = out
                l2 = l2.next    
        if (l1 or l2) and output is None:
            if l1:
                return l1 
            else:
                return l2
        elif l1:
            out.next = l1 
        elif l2:
            out.next = l2 
        return output    