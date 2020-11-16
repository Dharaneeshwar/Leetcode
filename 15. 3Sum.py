# Time Complexity => O(n^2 + log n) ; log n for sorting
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1 
            k = len(nums)-1 
            while j<k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    output.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1 
                elif temp>0:
                    k-=1 
                else:
                    j+=1
        return output            