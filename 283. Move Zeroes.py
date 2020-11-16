# Time Complexity : O(n)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read,write = 0,0 
        while read<len(nums) and write<len(nums):
            if nums[read]==0:
                read+=1 
            else:
                nums[write] = nums[read]
                write+=1
                read+=1
        while write<len(nums):
            nums[write] = 0
            write+=1