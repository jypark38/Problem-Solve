function solution(clothes) {
    var answer = 0;
    const dic={}
    for(c of clothes){
        if(dic.hasOwnProperty(c[1])){
            dic[c[1]].push(c[0])
        }else{
            dic[c[1]] = [c[0]]
        }
    }
    let a = 1
    for(t in dic){
        a*=(dic[t].length+1)
    }
    
    return a-1;
}