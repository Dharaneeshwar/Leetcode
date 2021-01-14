# Time Complexity : O(n) ; Space Complexity : O(n)

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        acc = [0] + list(accumulate(nums)) 
        goal = acc[-1] - x 
        arrlen = len(nums)
        maxarrlen = -1
        
        if goal < 0 :
            return -1 
        
        dairy = {}
        
        for i,val in enumerate(acc):
            dairy[val] = i 
        
        for i in dairy:
            if goal+i in dairy:
                maxarrlen = max(maxarrlen,dairy[goal+i]-dairy[i])
        
        return arrlen - maxarrlen if maxarrlen != -1 else -1