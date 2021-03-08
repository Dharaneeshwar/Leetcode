class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        s = list(s)
        ind = s.index('1')
        while ind<len(s) and s[ind] == '1':
            s[ind] = '0'
            ind += 1
        if '1' in s:
            return False 
        else:
            return True