function solution(board, moves) {
    var answer = 0;
    const stack = []
    const n = board.length
    zip= (rows) => rows[0].map((_,c)=>rows.map(row=>row[c]))
    
    const tBoard = zip(board)
    
    
    for(i=0;i<moves.length;i++){
        const pos = moves[i]
        let curr
        for(j=0;j<n;j++){
            if(tBoard[pos-1][j] === 0) continue
            curr = tBoard[pos-1][j]
            break;
        }
        if(!curr) continue
        tBoard[pos-1][j] = 0
        if(stack.length !== 0){
            if(stack[stack.length-1] === curr) {
                stack.length -= 1
                answer+=2
                continue
            }
        }
        stack.push(curr)
    }
    
    
    return answer;
}