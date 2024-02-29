function solution(arr) {
    const row = arr.length
    const col = arr[0].length
    if(row==col) return arr
    if(row<col){
        const newRow = Array.from({length:col}).fill(0)
        for(let i = row; i<col;i++) arr.push(newRow)
        return arr
    }
    const answer = arr.map(e=>{
        for(let i = col;i<row;i++) e.push(0)
        return e
    })
    return answer;
}