function solution(survey, choices) {
    var answer = '';
    const score = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    
    survey.forEach((e,idx)=>{
        const c = choices[idx]
        if (c!==4) {
        const idx = c>4 ? 1 : 0
        score[e[idx]] += Math.abs(4-c)
        }
    })
    for(let type of [['R','T'],['C','F'],['J','M'],['A','N']]){
        const [a,b] = type
        if(score[a]>=score[b]){
            answer+=a
        }else{
            answer+=b
        }
    }
    
    return answer;
}