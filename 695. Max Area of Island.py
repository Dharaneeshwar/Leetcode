class Solution:
    def dfs(self,grid,r,c,i,j):
        if i<0 or i>=r or j>=c or j<0:
            return
        if grid[i][j] == 1:
            self.area += 1
            grid[i][j] = 2
            self.dfs(grid,r,c,i-1,j)
            self.dfs(grid,r,c,i+1,j)
            self.dfs(grid,r,c,i,j-1)
            self.dfs(grid,r,c,i,j+1)    
                
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r,c  = len(grid),len(grid[0])
        maxarea = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    self.area = 0
                    self.dfs(grid,r,c,i,j)
                    maxarea = max(maxarea,self.area)
        return maxarea    