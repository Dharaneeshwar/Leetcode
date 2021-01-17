class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1 and i > 0:
                    matrix[i][j] += matrix[i-1][j]
            
            temp = sorted(matrix[i],reverse = True)
            
            for j in range(len(matrix[0])):
                ans = max(ans,temp[j] * (j+1))
        return ans