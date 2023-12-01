def solution(keyinput, board):
    answer = [0,0]
    w = (board[0]-1)//2
    h = (board[1]-1)//2
    
    for key in keyinput:
        if key[0] == 'l' and answer[0]>-w:
            answer[0]-=1
        if key[0] == 'r' and answer[0]<w:
            answer[0]+=1
        if key[0] == 'u' and answer[1]<h:
            answer[1]+=1
        if key[0] == 'd' and answer[1]>-h:
            answer[1]-=1
    
    return answer