function solution(n) {
    var answer = [];
    for(let i=0;i<n;i++) answer.push(Array(n).fill(0))
    const d = [[0,1],[1,0],[0,-1],[-1,0]]
    let d_idx = 0
    let x=-1,y=0;
    for(let i=1;i<=n*n;i++){
        let [dy,dx]= d[d_idx]
        let nx = x+dx
        let ny = y+dy
        if(nx>=n || nx<0 || ny>=n || ny<0 || answer[ny][nx]!==0){
            d_idx = (d_idx+1)%4
            let [dy,dx] = d[d_idx]
            nx = x+dx
            ny = y+dy
        }
        answer[ny][nx]=i
        x = nx
        y = ny
    }
    
    return answer;
}