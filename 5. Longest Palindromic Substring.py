# Brute Force - O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen, substr = 0, ""
        if len(s) == 1:
            return s
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                if len(s[i:j]) > maxlen and s[i:j] == s[i:j][::-1]:
                    substr = s[i:j]
                    maxlen = j-i
        return substr

# TODO : Better solution
