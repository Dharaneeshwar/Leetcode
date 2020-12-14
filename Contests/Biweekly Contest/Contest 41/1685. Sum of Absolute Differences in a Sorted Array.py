class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        accu = [nums[0]] 
        arrlen = len(nums)
        for i in range(1,arrlen):
            accu += [accu[-1]+nums[i]]
        print(accu)    
        out = []
        for i in range(arrlen):
            out.append(((nums[i]*i)-(nums[i]*(arrlen-i-1)) - (accu[i]-nums[i])+(accu[-1]-accu[i])))
        return out    