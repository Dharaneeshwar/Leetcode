class Solution:
    def beautySum(self, s: str) -> int:
        def calc(d):
            temp = d.values() 
            return max(temp) - min(temp)
        length = len(s)
        dairy = {}
        res = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                dairy[s[j]]= dairy.get(s[j],0)+1 
                res += calc(dairy)
            for j in range(i,len(s)):
                dairy[s[j]]-=1 
                if dairy[s[j]]==0:
                    del dairy[s[j]]
        return res