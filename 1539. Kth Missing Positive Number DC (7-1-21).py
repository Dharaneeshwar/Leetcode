class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = [] 
        limit = arr[-1] 
        nums = set(arr)
        for i in range(1,limit):
            if i not in nums:
                missing.append(i)
                 
        if len(missing) >= k:
            return missing[k-1]
        else:
            return limit + k - len(missing)