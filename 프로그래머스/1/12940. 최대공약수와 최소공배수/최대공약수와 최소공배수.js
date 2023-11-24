function solution(n, m) {
    var answer = [];
    var a,b
    for(let i=1;i<=Math.min(n,m);i++){
        if(n%i === 0 && m%i ===0) a = i
    }
    b = (Math.max(n,m) / a) * (Math.min(n,m) / a) * a

    return [a,b];
}