function solution(strArr) {
    var answer = strArr.map((e,i)=>i%2==0?e.toLowerCase():e.toUpperCase());
    return answer;
}