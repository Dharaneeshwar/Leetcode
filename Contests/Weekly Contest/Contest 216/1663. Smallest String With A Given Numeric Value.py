class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        string = ['a']*(n)
        ind = n-1
        k-=n
        while k>0:
            if k>=26:
                string[ind] = 'z'
                k -= 25 
            else:
                string[ind] = chr(97+k)
                k -= k  
            ind -= 1    
        return ''.join(string)    