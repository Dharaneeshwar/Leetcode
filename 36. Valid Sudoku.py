class Solution:
    def isValidSudoku(self, boards: List[List[str]]) -> bool:
        def checkrows():
            for i in range(len(boards)):
                dairy = set() 
                for num in boards[i]:
                    if num == ".":
                        continue 
                    if num in dairy:
                        return False 
                    dairy.add(num)
            return True
        
        def checkcols():
            for j in range(len(boards[0])):
                dairy = set() 
                for i in range(len(boards)):
                    num = boards[i][j]
                    if num == ".":
                        continue 
                    if num in dairy:
                        return False 
                    dairy.add(num)
            return True
        
        def checkgrids():
            dairylist = [set() for i in range(9)]
            for i in range(9):
                for j in range(9):
                    if boards[i][j] == '.':
                        continue
                    index = (i//3)*3 + j // 3
                    num = boards[i][j]
                    if num in dairylist[index]:
                        return False 
                    dairylist[index].add(num)
            return True        
        
        if checkrows() and checkcols() and checkgrids():
            return True 
        return False