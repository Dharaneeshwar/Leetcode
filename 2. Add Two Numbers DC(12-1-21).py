# Time Complexity - O(n) ; Space Complexity - O(n)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:        
        carry = 0 
        out = temp = ListNode()
        while l1 is not None and l2 is not None:
            tempsum = l1.val + l2.val
            tempsum += carry
            if tempsum > 9:
                carry = tempsum//10
                tempsum %= 10
            else:
                    carry = 0
            temp.next = ListNode(tempsum)
            temp = temp.next
            l1 = l1.next 
            l2 = l2.next
        if l1:
            while l1:
                tempsum = l1.val + carry
                if tempsum > 9:
                    carry = tempsum//10
                    tempsum %= 10
                else:
                    carry = 0
                temp.next = ListNode(tempsum)
                temp = temp.next
                l1 = l1.next
        elif l2:
            while l2:
                tempsum = l2.val + carry
                if tempsum > 9:
                    carry = tempsum//10
                    tempsum %= 10
                else:
                    carry = 0
                temp.next = ListNode(tempsum)
                temp = temp.next
                l2 = l2.next
        if carry:
            temp.next = ListNode(carry)
        return out.next