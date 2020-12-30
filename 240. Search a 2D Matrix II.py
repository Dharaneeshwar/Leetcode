class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # starting from bottom left 
        r,c  = len(matrix), len(matrix[0]) 
        i,j = r-1,0 
        while i>= 0 and j<c:
            if matrix[i][j] == target:
                return True 
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False         