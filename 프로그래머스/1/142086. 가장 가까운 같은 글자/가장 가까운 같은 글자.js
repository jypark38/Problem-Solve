function solution(s) {
    var answer = [];
    
    stack = []
    for(let i =0; i<s.length;i++){
        if(!stack.includes(s[i])) {
            answer.push(-1)
            stack.push(s[i])
        } else{
            
            _s = [...stack]
            stack.push(s[i])
            idx = _s.lastIndexOf(s[i])
            answer.push(i-idx)
        }
    }
    
    return answer;
}