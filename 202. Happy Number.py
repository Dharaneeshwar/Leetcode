class Solution:
    def isHappy(self, n: int) -> bool:
        count=0
        while n/10>0 and count<50: 
            su=0
            while n: 
                dig=n%10 
                su+=dig**2  
                n//=10
            n=su  
            print (n) 
            if n==1: 
                break 
            count+=1
        if n==1: 
            return True 
        else: 
            return False
       