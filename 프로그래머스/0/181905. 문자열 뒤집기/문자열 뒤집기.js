function solution(my_string, s, e) {
    var answer = '';
    const left = my_string.substr(0,s)
    const center = my_string.substr(s,e-s+1)
    const right = my_string.substr(e+1,)
    
    return left+[...center].reverse().join('')+right;
}