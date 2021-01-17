class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        result = 0 
        d=defaultdict(int)
        
        for i in range(len(nums)): 
            for j in range(i+1,len(nums)): 
                if d[nums[i]*nums[j]]>0: 
                
                    result+=(8*d[nums[i]*nums[j]])
                    
                d[nums[i]*nums[j]]+=1 
    
        return result