# Logical iterative solution ; 1068 ms
class Solution:
    def arrangeCoins(self, n: int) -> int:
        ind = 1
        while n>=0:
            n -= ind 
            if n>=0:
                ind += 1
        return ind-1    

# Binary Search ; 28 ms ; faster than 94.78 %
class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 0 
        end = n
        while start <= end:
            mid = start + (end-start)//2 
            value = (mid*(mid+1))//2
            if n == value:
                return mid 
            elif n < value:
                end = mid-1 
            else:
                start = mid+1
        return end         

# Mathematical ;
 
# According to sum of arithmetic series formula: 1 + 2 + 3 + ... + k = (1 + k) * k/ 2
# We can make quadratic equation out of it: (1 + k) * k/ 2 = n
# Meaning:
# k^2 + k - 2 * n = 0
# Which corresponds to general quadratic equation form:
# ax^2 + bx + c = 0

# By quadratic formula we can find: k = -b + sqrt(b^2 - 4ac)/2a
# Which in our case is: k = -1 + sqrt(1 + 8n)/2

# Answer is the solution of the equation taking the floor int value. 

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + (1+8*n)**0.5)//2)
