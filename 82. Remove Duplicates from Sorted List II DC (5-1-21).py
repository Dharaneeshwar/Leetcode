# O(n) Time Complexity ; O(n) Space Complexity

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dairy = {} 
        another_list = []
        while head:
            if head.val in dairy:
                dairy[head.val] += 1
            else:   
                dairy[head.val] = 1 
                another_list.append(head.val)
            head = head.next 
        ret = temp = ListNode(None)
        for val in another_list:
            if dairy[val] == 1:
                temp.next = ListNode(val)
                temp = temp.next
        return ret.next