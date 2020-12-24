# Time Complexity : O(n) ; Space Complexity : O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes = set() 
        while headA:
            nodes.add(headA)
            headA = headA.next 
        while headB:
            if headB in nodes:
                return headB 
            headB = headB.next 
        return None

# Time Complexity : O(2n) ; Space Complexity : O(1)
# Constant Space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lena,lenb = 0,0
        tempa,tempb = headA,headB
        while tempa:
            lena += 1
            tempa = tempa.next 
        while tempb:
            lenb += 1
            tempb = tempb.next 
        if lena>lenb:
            for i in range(lena-lenb):
                headA = headA.next
        elif lena<lenb:
            for i in range(lenb-lena):
                headB = headB.next 
        while headA and headB:
            if headA == headB:
                return headA 
            headA = headA.next
            headB = headB.next            
        return None

# Time Complexity : O(2n) ; Space Complexity : O(1) ; TRICKY
# Constant Space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lena,lenb = 0,0
        if headA == None or headB == None:
            return None

        A_pointer = headA
        B_pointer = headB

        while A_pointer != B_pointer:
            A_pointer = headB if A_pointer == None else A_pointer.next
            B_pointer = headA if B_pointer == None else B_pointer.next

        return A_pointer   
