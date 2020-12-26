# 28 ms ; faster than 86.36 %
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        dp[0] = 1 
        for i in range(1,len(s)+1):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if i>1 and s[i-2] > "09" and s[i-2] <= "26":
                dp[i] += dp[i-2]
        return dp[len(s)]        