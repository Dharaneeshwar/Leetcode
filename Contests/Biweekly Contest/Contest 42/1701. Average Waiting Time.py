class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start = customers[0][0] 
        wait = 0
        for i in range(len(customers)):
            
            end = max(start,customers[i][0]) + customers[i][1]
            wait += end - customers[i][0] 
            start = end 
        return wait/len(customers)