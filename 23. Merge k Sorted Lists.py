# I wish this algorithm passed all test cases. Unfortunately the final testcase gave TLE

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = out = ListNode(0)
        cond = True
        while cond:
            cond = False
            mini =  999 
            m_ind = -1
            for ind in range(len(lists)):
                node = lists[ind]
                if node is None: 
                    continue
                cond = True    
                if node.val < mini:
                    mini = node.val 
                    m_ind = ind
            if not cond:
                break
            if m_ind != -1:  
                out.next = ListNode(lists[m_ind].val)
                lists[m_ind] = lists[m_ind].next
                out = out.next
        return head.next

# TODO An Algorithm that passes