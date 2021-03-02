# 40 ms, faster than 100.00%
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        dairy = {}
        
        def possibleprices(cost,ind):
            if abs(target-cost) in dairy: 
                if dairy[abs(target-cost)] > cost:
                    dairy[abs(target-cost)] = cost 
            else:
                dairy[abs(target-cost)] = cost
            if ind>=len(toppingCosts) or cost-target > min(dairy):
                return
            possibleprices(cost,ind+1)
            possibleprices(cost+toppingCosts[ind],ind+1)
            possibleprices(cost+(toppingCosts[ind]*2),ind+1)
            
        for base in baseCosts:
            curCost = base 
            possibleprices(curCost,0)
        return dairy[min(dairy)]