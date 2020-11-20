# iteration O(log n) => 28ms

class Solution:
    def search(self, l: List[int], target: int) -> int:

        if not l:
            return -1 

        start, end = 0, len(l)-1 
        while start<=end:
            mid = start + ((end - start)//2)
            if l[mid] == target:
                return mid # returning index
            if l[mid]>=l[start] and l[mid]>=target and l[start]<=target:
                # if left part is sorted and target is in the left
                end = mid-1 
            elif l[mid]<=l[end] and l[mid]<=target and l[end]>=target:
                # if right part is sorted and target is in the right
                start = mid+1 
            elif l[mid]>=l[end]:
                # if right is not sorted
                start = mid+1 
            elif l[mid]<=l[start]:
                # if left is not sorted
                end = mid-1
            else: 
                return -1
        return -1    