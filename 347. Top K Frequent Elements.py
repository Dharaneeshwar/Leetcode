# Time Complexity - O(n log(n))
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dairy = {}
        # O(n)
        for num in nums:
            dairy[num] = dairy.get(num,0) + 1 
        # O(n log(n))
        unique = dairy.keys()
        unique.sort(key = lambda x:dairy[x])
        
        return unique[-k:]
        
# Time Complexity - O(n log(k))

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dairy = {}
        # O(n)
        for num in nums:
            dairy[num] = dairy.get(num,0) + 1 
        # O(n log(k))
        return heapq.nlargest(k,dairy.keys(),key = dairy.get)
 