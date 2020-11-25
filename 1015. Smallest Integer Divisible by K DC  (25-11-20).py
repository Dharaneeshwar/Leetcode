class Solution:
    def smallestRepunitDivByK(self, num: int) -> int:
        r = 0
        for l in range(1,num+1):
            r = (r*10+1) % num
            if r == 0:
                return l
        return -1