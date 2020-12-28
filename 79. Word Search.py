class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.findword(board,word,0,i,j,set())
        return self.found
        
    def findword(self,l,word,ind,i,j,visit):
        if self.found:
            return
        if i<0 or i>=len(l) or j<0 or j>=len(l[0]):
            return 
        if word[ind] == l[i][j] and (i,j) not in visit:
            visit.add((i,j))            
            if ind == len(word)-1:
                self.found = True 
                return
            else:
                self.findword(l,word,ind+1,i+1,j,visit)
                self.findword(l,word,ind+1,i-1,j,visit)
                self.findword(l,word,ind+1,i,j+1,visit)
                self.findword(l,word,ind+1,i,j-1,visit)
                visit.remove((i,j))
        return