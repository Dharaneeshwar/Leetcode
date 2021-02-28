class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mat = [[0 for j in range(len(text2)+1)] for j in range(len(text1)+1)]
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    mat[i][j] = mat[i-1][j-1] + 1
                else:
                    mat[i][j] = max(mat[i-1][j],mat[i][j-1])
        return mat[-1][-1]