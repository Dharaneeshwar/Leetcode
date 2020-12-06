class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort() 
        i = 0
        j = len(nums)-1 
        op = 0
        while i<j:
            val = nums[i] + nums[j]
            if val == k:
                op += 1 
                i += 1 
                j -= 1
            elif val > k:
                j -= 1
            else:
                i += 1
        return op        