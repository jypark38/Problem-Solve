function solution(arr, query) {
    var answer = [...arr];
    for(let i=0;i<query.length;i++) {
        
        const q = query[i]
        
        answer = i%2 ? answer.slice(q,) : answer.slice(0,q+1)
    }
    return answer;
}