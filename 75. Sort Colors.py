class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        red, white, blue = 0, 0, 0 
        for i in nums:
            if i==0:
                red += 1 
            elif i==1:
                white += 1 
            else:
                blue += 1
                
        # nums[:] = [0]*red + [1]*white + [2]*blue
        
        for i in range(red):
            nums[i] = 0 
        for i in range(red,red+white):
            nums[i] = 1 
        for i in range(red+white,red+white+blue):
            nums[i] = 2
        