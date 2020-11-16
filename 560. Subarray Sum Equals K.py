class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l=len(nums)
        count=0
        for i in range(l):
            s=0
            for j in range(i,l):
                s+=nums[j]
                if (s==k):
                    count+=1 
        return count        