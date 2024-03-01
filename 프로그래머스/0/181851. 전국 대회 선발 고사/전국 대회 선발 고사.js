function solution(rank, attendance) {
    var answer = 0;
    const newRank = rank.map((e,idx)=>[e,idx])
    const arr = newRank.filter((e)=>attendance[e[1]]).sort((a,b)=>a[0]-b[0])
    return 10000*arr[0][1]+100*arr[1][1]+arr[2][1];
}