class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0 
        i,j = len(num1)-1, len(num2)-1
        result = []
        while i>=0 or j>=0:
            tempsum = carry 
            if i>=0:
                tempsum += int(num1[i])
                i-=1
            if j>=0:
                tempsum += int(num2[j])
                j-=1    
            result.append(str(tempsum%10))
            carry = tempsum // 10
            
        if carry > 0:
            result.append(str(carry))
        
        return ''.join(result[::-1])
                