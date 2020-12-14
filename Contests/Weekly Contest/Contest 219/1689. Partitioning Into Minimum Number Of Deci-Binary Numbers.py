class Solution:
    def minPartitions(self, n: str) -> int:
        n = sorted(n) 
        count = 0 
        base = 0
        for i in n:
            count+=int(i)-base  
            base = int(i) 
        return count    

# One liner 

class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n)) 