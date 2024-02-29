function solution(board, k) {
    var answer = 0;
    const l = board.length
    const l2 = board[0].length
    for(let i=0;i<l;i++){
        for(let j=0;j<l2;j++){
            if(i+j<=k) answer+=board[i][j]
        }
    }
    return answer;
}