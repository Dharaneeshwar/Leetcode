# Random BruteForce Solution ; 1336 ms

class Solution:
    binary = ['1'] 
    def concatenatedBinary(self, n: int) -> int:
        res = ""
        for i in range(1,n+1):
            res+=bin(i)[2:]
        return int(res,2)%(10**9 + 7)

# Efficient on multiple testcases ; 292 ms

class Solution:
    binary = ['1'] # storing the binary values 
    def concatenatedBinary(self, n: int) -> int:
        if n <= len(self.binary):
            return int(''.join(self.binary[:n]),2)%1000000007 # using stored values from the previous testcase
        else:    
            for i in range(len(self.binary)+1,n+1):
                self.binary.append(bin(i)[2:]) 
            return int(''.join(self.binary),2)%1000000007
        