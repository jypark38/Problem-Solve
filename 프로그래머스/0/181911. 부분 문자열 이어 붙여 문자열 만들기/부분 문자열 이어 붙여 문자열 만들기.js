function solution(my_strings, parts) {
    var answer = '';
    my_strings.forEach((c,i)=>{
        [s,e] = parts[i]
        answer+=c.slice(s,e+1)
    })
    return answer;
}