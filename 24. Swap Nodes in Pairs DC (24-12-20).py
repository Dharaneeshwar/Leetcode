# 24 ms ; faster than 94.70 % ; Time Complexity - O(n)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev, prev.next = ListNode(0), head 
        ret = prev
        while prev.next and prev.next.next:
            a = prev.next 
            b = prev.next.next 
            prev.next, a.next, b.next = b, b.next, a
            prev = a 
        return ret.next