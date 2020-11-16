class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=nums[0]
        for i in range(1,len(nums)):
            s^=nums[i]
        return s