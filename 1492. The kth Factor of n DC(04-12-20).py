class Solution:
    def get_factors(self,n):
        f  = [] 
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                f.append(i)
                if n//i != i:
                    f.append(n//i)
        return sorted(f) 
                   
    def kthFactor(self, n: int, k: int) -> int:
        facts = self.get_factors(n)
        if len(facts) < k:
            return -1
        print(facts)
        return facts[k-1]