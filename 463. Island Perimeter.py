class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    peri += 4
                    if i+1 < len(grid) and grid[i+1][j] == 1:
                        peri -= 2
                    if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                        peri -= 2 
        return peri                