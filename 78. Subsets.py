# RECURSIVE ; using a helper method to do the job
class Solution:
    l = [] # class member
    def subset_helper(self,nums,index,subset):
        if index == len(nums):
            self.l.append(subset) # acessing l using self
            return
        self.subset_helper(nums,index+1,subset+[nums[index]]) # adding curent element 
        self.subset_helper(nums,index+1,subset) # ignoring current element
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.l = [] 
        # initializing l as empty [] because the same function will be called by leetcode for multiple testcases and the l will not be reinitialized
        self.subset_helper(nums,0,[])

        return self.l # return l