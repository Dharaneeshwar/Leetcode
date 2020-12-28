# 24 ms ; faster than 98.95 % ; Backtracking ; using arrays because its efficient in manipulating over strings
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = [] 
        def backtrack(s,left,right):
            if len(s) == n*2:
                out.append("".join(s))
            if left<n:
                backtrack(s+['('],left+1,right)
            if right<left:
                backtrack(s+[')'],left,right+1)
        
        backtrack([],0,0)
        
        return out