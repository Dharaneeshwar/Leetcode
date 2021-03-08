class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        globalmindist = float('inf') 
        globalminind = -1 
        for ind,point in enumerate(points):
            if point[0] == x or point[1] == y:
                temp_dist = (abs(point[0] - x)+abs(point[1]-y))
                if temp_dist < globalmindist:
                    globalmindist = temp_dist 
                    globalminind = ind 
        return globalminind
        