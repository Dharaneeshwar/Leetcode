# Time : O(n) ; Space : O(n)

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        out = [] 
        for i,n in enumerate(nums):
            while out and out[-1] > n and k-len(out)+i < len(nums):
                out.pop() 
            out.append(n)
        return out[:k]