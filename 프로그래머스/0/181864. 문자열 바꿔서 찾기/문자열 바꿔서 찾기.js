function solution(myString, pat) {
    var answer = '';
    for(c of myString){
        answer += c == 'A' ? 'B' : 'A'
    }
    return +(answer.includes(pat));
}