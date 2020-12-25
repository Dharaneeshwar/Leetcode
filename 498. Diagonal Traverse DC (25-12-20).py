class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        l = [[] for i in range(len(matrix)+len(matrix[0])-1)] 
        out = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                l[i+j].append(matrix[i][j])
                
        for i in range(len(l)):
            if i%2==1:
                for j in l[i]:
                    out.append(j)
            else:
                for j in reversed(l[i]):
                    out.append(j)
        return out             