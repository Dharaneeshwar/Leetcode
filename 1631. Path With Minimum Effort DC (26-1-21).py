from heapq import heappop, heappush
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row,col = len(heights),len(heights[0])
        
        dist = [[float('inf')]*col for i in range(row)]
        
        heap = [] 
        heap.append((0,0,0))
        
        dirs = [0,1,0,-1,0]
        
        while heap:
            
            d, r, c = heappop(heap)
            
            if d > dist[r][c]:
                continue 
            
            if r == row-1 and c == col-1:
                return d
            
            for i in range(4):
                new_row, new_col = r + dirs[i], c + dirs[i+1] 
                
                if 0 <= new_row < row and 0 <= new_col < col:
                    new_dist = max(d,abs(heights[new_row][new_col] - heights[r][c]))
                    
                    if new_dist < dist[new_row][new_col]:
                        dist[new_row][new_col] = new_dist 
                        heappush(heap,(new_dist,new_row,new_col))
                    