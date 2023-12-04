def solution(board):
    answer = 0
    b = len(board)**2
    d = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]
    w = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                w+=1
                for dx,dy in d:
                    if (i+dx) < 0 or (i+dx) >= len(board):
                        continue
                    if (j+dy) < 0 or (j+dy) >= len(board):
                        continue
                    if  board[i+dx][j+dy] == 0:
                        board[i+dx][j+dy] = 2
                        w+=1
    
    return b-w