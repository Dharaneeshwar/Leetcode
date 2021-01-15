class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0,1]
        for i in range(2,n+1,2):
            ind = i//2
            nums.append(nums[ind])
            nums.append(nums[ind]+nums[ind+1])
        print(nums)
        return max(nums[:n+1])