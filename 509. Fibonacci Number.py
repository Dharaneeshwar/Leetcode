# Typical Recursion ; 996ms ; faster that 9.17 %
class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0 
        if N==1:
            return 1 
        return self.fib(N-1) + self.fib(N-2)

# Iterative Solution ; 28ms ; faster than 76.79 %
class Solution:
    def fib(self, N: int) -> int:
        first, second = 0,1 
        if N==0:
            return first 
        if N==1:
            return second 
        f = 0
        for i in range(N-1):
            f = first + second 
            first,second = second, f
        return f    

# Effient Solution (Hashes) ; 12ms ; faster than 99.96 % 
class Solution:
    def fib(self, N: int) -> int:
        hash_dict = {
            0:0, 
            1:1
        }
        return self.fib_helper(N,hash_dict)
    
    def fib_helper(self,N,hash_dict):
        if N in hash_dict:
            return hash_dict[N]
        else:
            hash_dict[N] = self.fib_helper(N-1,hash_dict) + self.fib_helper(N-2,hash_dict)
            return hash_dict[N]
