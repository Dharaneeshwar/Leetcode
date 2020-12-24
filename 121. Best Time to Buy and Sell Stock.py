# One Pass ; 56 ms ; faster than 90.06 %
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0    
        globalprofit = 0 
        mini = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if mini > prices[i]:
                mini = prices[i]
            if prices[i]-mini > profit:    
                profit = prices[i]-mini 
            if globalprofit < profit:
                globalprofit = profit 
        return globalprofit         