function solution(n, k) {
    var answer = [k];
    for(let i=1;i<Math.floor(n/k);i++){
        answer.push(answer[i-1]+k)
    }
    return answer;
}