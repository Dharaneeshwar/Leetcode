# DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins.sort()
        dp = [amount+1 for i in range(amount+1)]
        dp[0] = 0 
        for i in range(1,amount+1):
            for j in range(n):
                if coins[j] > i:
                    break 
                dp[i] = min(dp[i], 1 + dp[i-coins[j]])
        return dp[amount] if dp[amount] != amount+1 else -1       