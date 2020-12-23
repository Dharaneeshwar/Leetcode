# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s,e = 1,n 
        while s<=e:
            mid = s + (e-s)//2
            isbad = isBadVersion(mid)
            if isbad and (not isBadVersion(mid-1) or mid-1 == -1):
                return mid
            elif isbad:
                e = mid-1
            else:
                s = mid+1
            