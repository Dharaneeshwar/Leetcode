class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        value = sum(nums)
        goal -= value
        goal = abs(goal)
        res=0
        while goal: 
            if goal<limit: 
                return res+1 
            else: 
                res += (goal//limit) 
                goal %= limit
            if goal == 0: 
                return res
        return res