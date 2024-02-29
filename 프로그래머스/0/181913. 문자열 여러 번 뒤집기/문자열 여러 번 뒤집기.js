function solution(my_string, queries) {
    var answer = my_string;
    for (q of queries){
        const left = answer.slice(0,q[0])
        const center = answer.slice(q[0],q[1]+1)
        const right = answer.slice(q[1]+1)
    
        answer = left + [...center].reverse().join('') + right
    }
    return answer;
}