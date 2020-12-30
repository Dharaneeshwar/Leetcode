class Solution:
    def findpath(self,grid,i,j,canwalk):
        if i<0 or i >= len(grid) or j<0 or j>= len(grid[0]):
            return 
        if grid[i][j] == -1:
            return 
        if grid[i][j] == 2:
            if canwalk==1:
                self.noofpath += 1
            return 
        value = grid[i][j]
        grid[i][j] = -1
        self.findpath(grid,i+1,j,canwalk-1)
        self.findpath(grid,i-1,j,canwalk-1)
        self.findpath(grid,i,j+1,canwalk-1)
        self.findpath(grid,i,j-1,canwalk-1)
        grid[i][j] = value
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        self.noofpath = 0
        canwalk = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    x,y = i,j 
                if grid[i][j] != -1:
                    canwalk+=1
        self.findpath(grid,x,y,canwalk)
        return self.noofpath            