# One Pass ; 56 ms ; faster than 90.06 %
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0    
        globalmin = prices[0] 
        globalprofit = 0 
        tempmin = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if tempmin > prices[i]:
                tempmin = prices[i]
            if prices[i]-tempmin > profit:    
                profit = prices[i]-tempmin 
            if globalprofit < profit:
                globalprofit = profit 
                globalmin = tempmin
        return globalprofit         