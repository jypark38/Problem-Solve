function solution(intStrs, k, s, l) {
    const answer = []
    for(c of intStrs){
        let result = ''
        const end = c.length<s+l ? c.length : s+l
        for(let i=s;i<end;i++){
            result += c[i]
        }
        result*=1
        if(result>k) answer.push(result)
    }
    return answer
}