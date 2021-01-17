class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        output = 0 
        dairy = {} 
        
        for num in deliciousness:
            dairy[num] = dairy.get(num,0) + 1 
        
        for i in range(31):
            for j in deliciousness:
                if int(2**i) - j in dairy:
                    output += dairy[int(2**i)-j]
                    
                    if int(2**i)-j == j:
                        output -= 1
                        
                        
        output //= 2
        
        return output%(10**9+7)