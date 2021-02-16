class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = []
        def dfs(s,temp,ind,result):
            if ind == len(s):
                result.append(temp)
                return
            if s[ind].isalpha():
                dfs(s,temp+s[ind],ind+1,result)
                dfs(s,temp+(s[ind].swapcase()),ind+1,result)
            else:
                dfs(s,temp+s[ind],ind+1,result)
        dfs(S,"",0,result) 
        
        return result