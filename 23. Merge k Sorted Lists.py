# TLE

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
            mini =  float('inf') 
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

# using minheap

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = temp = ListNode(None)
        heap = [(node.val,ind,node) for ind,node in enumerate(lists) if node]
        
        heapq.heapify(heap)
        
        while heap:
            # adding index is the key, because we are passing the node and comparision of node and node is not allowed in python 3
            # Therefore when there is a duplicate number in all nodes the comparision tries to compare based on node which is not allowed so adding index of the list avoids the comparison of nodes
            val,ind,node = heapq.heappop(heap)
            temp.next = ListNode(val)
            temp = temp.next
            node = node.next 
            if node:
                heapq.heappush(heap,(node.val,ind,node))
        return head.next         