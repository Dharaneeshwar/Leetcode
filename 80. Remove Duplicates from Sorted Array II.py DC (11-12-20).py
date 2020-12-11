# Two Pointer approch ;
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arrlen = len(nums)
        if arrlen <= 2:
            return arrlen
        fast = 2
        slow = 2 
        while fast<arrlen:
            if nums[slow-2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast+=1     
        return slow     
