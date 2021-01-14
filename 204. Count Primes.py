class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True]*n
        
        i = 2 
        while i*i < n:
            if primes[i]:
                j = i 
                while i*j < n:
                    primes[i*j] = False
                    j += 1
            i += 1 
            
        return primes[2:].count(True)