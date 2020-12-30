# 80 ms ;  faster than 85.96 %  
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = 0 
        j = len(nums) 
        left = -1 
        right = -1
        while i<j:
            mid  = (i+j)//2 
            if nums[mid] == target:
                if mid == 0 or (mid>0 and nums[mid-1] != target):
                    left = mid
                    break
                else:
                    j = mid 
            elif nums[mid] < target:
                i = mid+1 
            else:
                j = mid
        if left == -1:
            return [-1,-1]    
        i = 0 
        j = len(nums) 
        while i<j:
            mid  = (i+j)//2 
            if nums[mid] == target:
                if mid == len(nums)-1 or (mid < len(nums)-1 and nums[mid+1] != target):
                    right = mid
                    break
                else:
                    i = mid+1 
            elif nums[mid] < target:
                i = mid+1 
            else:
                j = mid
        return [left,right]