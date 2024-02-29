function solution(numLog) {
    var answer = '';
    for(let i=1;i<numLog.length;i++){
        const d = (numLog[i] - numLog[i-1])
        if (d==1){
            answer+='w'
        } else if(d==-1){
            answer+='s'
        } else if(d==10){
            answer+='d'
        } else{
            answer+='a'
        }
    }
    return answer;
}