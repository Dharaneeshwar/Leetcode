class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        square = {} 
        for i in rectangles:
            edge = min(i)
            square[edge] = square.get(edge,0) + 1 
        
        return square[max(square)]