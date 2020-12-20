class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ind = len(digits) - 1
        for ind in range(ind,-1,-1):
            num = digits[ind]
            if num == 9:
                digits[ind] = 0 
            else:
                digits[ind] = num+1 
                break
        else:
            return [1] + digits 
        return digits