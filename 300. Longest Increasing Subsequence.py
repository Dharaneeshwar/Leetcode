class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        count = [1]*len(nums)
        sequence = [-1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if count[j] + 1 > count[i] and nums[i] > nums[j]:
                    count[i] = count[j] + 1
                    sequence[i] = j
        return max(count)