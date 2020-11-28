# 48 ms ; faster than 80.94 % 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0 
        end = len(nums)-1 
        while start<end:
            mid = start + (end-start)//2
            if nums[start] > nums[mid]:
                end = mid 
            elif nums[end] < nums[mid]:
                start = mid + 1 
            else:
                end -= 1 
        return nums[start]        
                    