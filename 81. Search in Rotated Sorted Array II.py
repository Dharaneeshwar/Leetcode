# Solution for rotated sorted numbers with duplicates

# 53 ms ;  faster than 62.49 % submissions

class Solution:
    def search(self, l: List[int], target: int) -> bool:

        if not l:
            return False 

        start, end = 0, len(l)-1 
        while start<=end:
            mid = start + ((end - start)//2)

            if l[mid] == target: # found
                return True 

            if l[mid]>l[start] and l[mid]>target and l[start]<=target: 
                # if left part is sorted and target is in the left
                end = mid-1 
            elif l[mid]<l[end] and l[mid]<target and l[end]>=target:
                # if right part is sorted and target is in the right
                start = mid+1 
            elif l[mid]>l[end]:
                # if right is not sorted
                start = mid+1 
            elif l[mid]<l[start]:
                # if left is not sorted
                end = mid-1
            else: 
                # if we can't figure out which side of the array has the element
                # But, its not on the endpoints
                end-=1 
                start+=1
        # the array has been checked 
        return False    