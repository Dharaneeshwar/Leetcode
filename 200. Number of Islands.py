# 128 ms ;  faster than 90.66 %
class Solution:
    def dfs(self,grid,r,c,i,j):
        if i<0 or i>=r or j>=c or j<0:
            return
        if grid[i][j] == '1':
            grid[i][j] = 'visited'
            self.dfs(grid,r,c,i-1,j)
            self.dfs(grid,r,c,i+1,j)
            self.dfs(grid,r,c,i,j-1)
            self.dfs(grid,r,c,i,j+1)    
                
    def numIslands(self, grid: List[List[str]]) -> int:
        r,c  = len(grid),len(grid[0])
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid,r,c,i,j)
        return count            