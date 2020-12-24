class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dairy = {} 
        dairy2 = {}
        for i in s:
            dairy[i] = dairy.get(i,0) + 1 
        for i in t:
            dairy2[i] = dairy2.get(i,0) + 1 
        
        for i in list(dairy.keys()) + list(dairy2.keys()):
            count = dairy.get(i,-1)
            count2 = dairy2.get(i,-1)
            if count == -1 or count2 == -1:
                return False 
            elif count != count2:
                return False
        return True        
            