# TLE ; Recursive
class Solution:
    l = [] 
    def subset_helper(self,nums,index,subset,k):
        if index == len(nums):
            if len(subset) == k :
                if (subset < self.l or len(self.l)==0):
                    self.l = subset
            return
        self.subset_helper(nums,index+1,subset+[nums[index]],k) # adding curent element 
        self.subset_helper(nums,index+1,subset,k) # ignoring current element
        
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        self.l = []
        self.subset_helper(nums,0,[],k)
        return self.l

# DP Solution

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        out = [] 
        for i in range(len(nums)):
            while len(out)>0 and out[-1] > nums[i] and len(out)+len(nums)-i-1 >= k:
                out.pop()
            out.append(nums[i]) 
        return out[:k]     