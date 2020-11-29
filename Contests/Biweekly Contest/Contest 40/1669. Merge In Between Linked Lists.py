# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = list1 
        for i in range(a-1):
            start = start.next 
        print(start.val)
        end = start
        for i in range(b-a+2):
            end = end.next 
        print(end.val)    
        start.next = list2 
        while list2.next:
            list2 = list2.next 
        list2.next = end 
        return list1