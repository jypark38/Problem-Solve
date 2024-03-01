function solution(dartResult) {
    var answer = 0;
    const scores = [0,0,0,0]
    let result = ''
    const BONUS = {'S':1,'D':2,'T':3}
    for(let i=0;i<dartResult.length;i++){
        const c = dartResult[i]
        
        if(c==1 && dartResult[i+1]=='0'){
            result += '^10'
            i+=1
        }else if(c>='0'&& c<='9'){
            result += `^${c}`
        }else{
            result+=c
        }
    }
    result = result.split('^')
    for(let i=1;i<result.length;i++){
        let score = ''
        let bonus = ''
        let option = ''
        for(let c of result[i]){
            if(c>='0' && c<='9'){
                score+=c                
            }else if(c=='S' || c=='T' || c=='D'){
                bonus = c
            }else{
                option=c
            }
        }
        score*=1
        scores[i] = Math.pow(score,BONUS[bonus])
        if(option=='*'){
            scores[i-1] *= 2
            scores[i] *= 2
        }
        if(option=='#'){
            scores[i] *= -1
        }
    }
    return scores.reduce((a,b)=>a+b)
}