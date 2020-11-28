# 16 ms ; 99.92 ms
class Solution:
    
    def fact(self,no): # find factorial
        if no in [0,1]:
            return 1 
        else:
            return no * self.fact(no-1)
        
    def permu_helper(self,nums,k,result): # helper method

        # exit condition
        if len(nums) == 0:
            return
        
        # maths logic
        b_len = self.fact(len(nums)-1)
        ind = (k-1) // b_len
        result += str(nums[ind]) 
        nums.pop(ind)
        k -= (ind * b_len) 
        
        self.permu_helper(nums,k,result)
        
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1,n+1)) 
        result = [] 
        self.permu_helper(nums,k,result) 
        return ''.join(result)