# One Liner ; O(n logn)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(list(map(lambda x:x*x,nums)))