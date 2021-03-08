class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        noOfTypes = len(set(candyType)) 
        maximumEatable = len(candyType)//2 
        return min(noOfTypes,maximumEatable)