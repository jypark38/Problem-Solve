function solution(lottos, win_nums) {
    var answer = [];
    let s=0,f=0;
    const rank = [6,6,5,4,3,2,1]
    for(n of lottos){
        if(n==0){
            s+=1
            f+=1
            continue
        }
        if(win_nums.includes(n)){
            s+=1
        }else{
            f+=1
        }
    }
    f=6-f
    
    return [rank[s],rank[f]]
}