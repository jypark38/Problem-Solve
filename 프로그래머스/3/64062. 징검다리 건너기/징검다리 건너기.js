function solution(stones, k) {
    var answer = []
    let start=0, end =200000000
    return bs(start,end,stones,k)
}

function bs(start,end,stones,k){
    //종료조건
    if(start==end) return start
    let mid = parseInt((start+end)/2)
    let cnt = 0
    for(i=0;i<stones.length;i++){
        if(stones[i]<=mid){
            cnt++
        }else{
            cnt=0
        }
        if(cnt>=k) break
    }
    if(cnt===k){
        return bs(start,mid,stones,k)
    }else{
        return bs(mid+1,end,stones,k)
    }
}