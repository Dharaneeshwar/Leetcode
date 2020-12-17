class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        arrlen = len(nums)
        nums.sort()
        out = []
        for i in range(arrlen-3):
            js = i+1   
            for j in range(js,arrlen-2):
                left = j+1 
                right = len(nums)-1 
                while left<right:
                    tot = nums[i]+nums[j]+nums[left]+nums[right]
                    if tot == target and [nums[i],nums[j],nums[left],nums[right]] not in out:
                        out.append([nums[i],nums[j],nums[left],nums[right]])
                    elif tot < target:
                        left+=1 
                    else:
                        right-=1
        return out         