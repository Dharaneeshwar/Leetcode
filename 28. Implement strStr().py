# using predefined methods

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

# without index method
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0 
        j = 0 
        if len(needle) == 0:
            return 0 
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1