function solution(maps) {
    var answer = [];
    const q = [[0,0]]
    let tx=maps.length,ty=maps[0].length
    const dx = [-1,1,0,0]
    const dy = [0,0,1,-1]
    while(q.length){
        [x,y] = q.shift()
        for(let i=0; i<4;i++){
            nx = dx[i]+x
            ny = dy[i]+y
            if ((ny>=0 && ny<ty)&& (nx>=0 && nx<tx)){
                if(maps[nx][ny]===1){
                    maps[nx][ny] = maps[x][y]+1;
                    q.push([nx,ny])
                }            
            }
        }
    }
    if(maps[tx-1][ty-1] > 1){
        return maps[tx-1][ty-1]
    }else{
        return -1
    }
}
