class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0])
        for i in range(r):
            for j in range(c):
                count = 0 
                for x in range(max(0,i-1),min(i+2,r)):
                    for y in range(max(0,j-1),min(j+2,c)):
                        if (x!= i or y!=j) and board[x][y] in [1,-1]:
                            count += 1    
                            
                if board[i][j] == 1:
                    if count < 2:
                        board[i][j] = -1
                    elif count in [2,3]:
                        board[i][j] = 1 
                    else:
                        board[i][j] = -1 
                else:
                    if count == 3:
                        board[i][j] = 2
        for i in range(r):
            for j in range(c):
                if board[i][j] == 2:
                    board[i][j] = 1 
                if board[i][j] == -1:
                    board[i][j] = 0
                    