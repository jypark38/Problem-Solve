function solution(l, r) {
    var answer = [];
    const rLength = r.toString().length
    const maxLen = parseInt(('1'.repeat(rLength))*1,2)
    
    for(let i=1;i<=maxLen;i++){
        const n = i.toString(2)*5
        if(n>=l && n<=r){
            answer.push(n)
        }
    }
    
    if (answer.length==0) return [-1]
    
    return answer;
}