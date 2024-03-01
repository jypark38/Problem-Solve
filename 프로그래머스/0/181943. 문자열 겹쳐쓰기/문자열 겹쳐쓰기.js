function solution(my_string, overwrite_string, s) {
    var answer = '';
    
    const left = my_string.substr(0,s)
    const right = my_string.substr(s+overwrite_string.length)
    
    return left+overwrite_string+right;
}