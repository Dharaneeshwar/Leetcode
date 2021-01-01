class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastpos = len(nums)-1 
        for i in range(len(nums)-1,-1,-1):
            if nums[i] + i >= lastpos:
                lastpos = i 
        return lastpos == 0        