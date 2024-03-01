function solution(board, moves) {
    var answer = 0;
    const stack = [-1]
    const N = board.length
    let endS = 0
    for(m of moves){
        let cr = m-1
        for(let i=0;i<N;i++){
            if(board[i][cr] != 0){
                stack.push(board[i][cr])
                board[i][cr] = 0
                endS++
                break
            }
        }
        if(stack[endS] == stack[endS-1]){
            stack.pop()
            stack.pop()
            answer+=2
            endS-=2
        }
    }
    return answer;
}