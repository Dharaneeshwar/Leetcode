# Recursion ; TLE
class Solution:
    def helper(self,l,ind,s):
        if ind==len(l):
            if s==0:
                self.c += 1
            return
        for i in range(len(l[ind])):
            self.helper(l,ind+1,s+l[ind][i])
    
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        self.c = 0
        # return 0
        self.helper([A,B,C,D],0,0)
        return self.c

# Iterative using Dictionary ; PASSED 

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        c = 0
        dairy = {} 
        arrlen = len(A)
        for i in A:
            for j in B:
                if i+j in dairy:
                    dairy[i+j] += 1 
                else:    
                    dairy[i+j] = 1
        for i in C:
            for j in D:
                expect = -(i+j)
                if expect in dairy:
                    c += dairy[expect]
        return c            