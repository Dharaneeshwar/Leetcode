class Solution:
    l = [] # class member
    def subset_helper(self,nums,index,subset):
        if index == len(nums):
            if subset not in self.l:
                self.l.append(subset) # acessing l using self
            return
        self.subset_helper(nums,index+1,subset+[nums[index]]) 
        self.subset_helper(nums,index+1,subset) 
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.l = [] 
        self.subset_helper(sorted(nums),0,[])
        
        return (self.l)