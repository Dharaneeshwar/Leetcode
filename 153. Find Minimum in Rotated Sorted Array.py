# using binary search (Recursion) : O(log n)

class Solution:
    def minimumHelper(self,arr,start,end):
        if start>end:
            return -1  # exit condition
        
        mid = int(start + (end-start)//2)
        
        if start < mid:
            if arr[mid] < arr[mid-1]:
                return mid
        
        if end > mid:
            if arr[mid] > arr[mid+1]:
                return mid+1 
        
        if arr[end] > arr[mid]:
            return self.minimumHelper(arr,start,mid-1)
        return self.minimumHelper(arr,mid+1,end)    
    
    def findMin(self, nums: List[int]) -> int:    
        if nums[0] <nums[len(nums)-1]:
            return nums[0]
        ind = self.minimumHelper(nums,0,len(nums)-1)
        return nums[ind]
    
# using binary search (Iterative) : O(log n)

class Solution:
    def findMin(self, nums: List[int]) -> int:    
        if nums[0] <= nums[len(nums)-1]:
            return nums[0]
        start = 0 
        end = len(nums)-1 
        while start <= end:
            mid = start + (end-start)//2
            if start < mid:
                if nums[mid] < nums[mid-1]:
                    return nums[mid]
        
            if end > mid:
                if nums[mid] > nums[mid+1]:
                    return nums[mid+1] 
        
            if nums[end] > nums[mid]:
                end = mid-1
            else:
                start = mid+1 
    
