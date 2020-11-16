# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        if temp.next == None:
            if n == 1:
                head = None
        elif temp.next.next == None:
            if n == 1:
                head.next = None
                return head
            if n == 2:
                head = head.next
                return head
        while temp != None:
            c = 0
            count = temp
            while count.next != None:
                c += 1
                count = count.next
            if head == temp and c+1 == n:
                head = head.next
                return head
            if c == n:
                temp.next = temp.next.next
                break
            temp = temp.next
        return head
