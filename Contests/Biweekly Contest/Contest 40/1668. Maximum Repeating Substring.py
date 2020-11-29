class Solution:
    def maxRepeating(self, s: str, sub: str) -> int:
        countarr = [0] 
        count = 0
        i = 0
        while i<(len(s)-len(sub)+1):
            print(s[i:i+len(sub)])
            if sub == s[i:i+len(sub)]:
                count = 0 
                while sub == s[i:i+len(sub)]:
                    count+=1
                    i += len(sub) 
                countarr.append(count)    
            else:
                i+=1    
        return max(countarr)