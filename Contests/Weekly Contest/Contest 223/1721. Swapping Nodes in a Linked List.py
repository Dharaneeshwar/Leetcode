# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        l = [] 
        while head:
            l.append(head.val)
            head = head.next 
        l[k-1], l[-k] = l[-k], l[k-1]    
        ret = temp = ListNode()
        for i in l:
            temp.next = ListNode(i)
            temp = temp.next
        return ret.next