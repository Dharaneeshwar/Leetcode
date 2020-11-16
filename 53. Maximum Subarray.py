class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max=nums[0]
        global_max=nums[0]
        for i in range(1,len(nums)):
            current_max=max(nums[i],current_max+nums[i])
            global_max=max(current_max,global_max)
        return global_max