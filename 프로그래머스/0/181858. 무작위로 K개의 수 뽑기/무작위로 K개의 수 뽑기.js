function solution(arr, k) {
    var answer = [];
    for(let i=0;i<arr.length;i++){
        if (answer.length === k) break;
        if (answer.includes(arr[i])) continue
        answer.push(arr[i])
    }
    while (answer.length !== k){
        answer.push(-1)
    }
    return answer;
}