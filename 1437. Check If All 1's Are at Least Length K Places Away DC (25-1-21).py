# 540 ms ; faster than 94.41 % ; Time - O(n) ; Space - O(1)
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -k-1 
        for ind,n in enumerate(nums):
            if n == 1:
                if ind - prev >= k+1:
                    prev = ind 
                else:
                    return False
        return True
