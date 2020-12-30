class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    continue 
                temp = []    
                if i>0:
                    temp.append(grid[i-1][j])
                if j>0:
                    temp.append(grid[i][j-1])
                grid[i][j] += min(temp)   
        return grid[-1][-1]            