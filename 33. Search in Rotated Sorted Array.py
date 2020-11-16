# iteration O(log n) => 28ms
class Solution:
    def search(self, l: List[int], target: int) -> int:
        if len(l)==1:
            if l[0]!=target:
                return -1 
            else:
                return 0
        if len(l)==0:
            return -1 
        start, end = 0, len(l)-1 
        while start<=end:
            mid = start + ((end - start)//2)
            if l[mid] == target:
                return mid 
            if l[mid]>=l[start] and l[mid]>=target and l[start]<=target:
                end = mid-1 
            elif l[mid]<=l[end] and l[mid]<=target and l[end]>=target:
                start = mid+1 
            elif l[mid]>=l[end]:
                start = mid+1 
            elif l[mid]<=l[start]:
                end = mid-1
            else: 
                return -1
        return -1    