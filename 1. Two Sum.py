# Brute Force - O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]


# Time Complexity - O(n) ; Space Complexity - O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashes = {}
        
        for ind,num in enumerate(nums):
            other_num = target - num 

            if other_num in hashes:
                return [hashes[other_num],ind]

            hashes[num] = ind        