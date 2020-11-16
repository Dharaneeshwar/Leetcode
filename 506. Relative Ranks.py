#  Time Complexity O(n logn)
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        d = {}
        temp = sorted(nums, reverse=True)
        for i in nums:
            d[i] = temp.index(i)
        for i in range(len(nums)):
            if d[nums[i]] == 0:
                nums[i] = "Gold Medal"
            elif d[nums[i]] == 1:
                nums[i] = "Silver Medal"
            elif d[nums[i]] == 2:
                nums[i] = "Bronze Medal"
            else:
                nums[i] = str(d[nums[i]]+1)
        return nums
