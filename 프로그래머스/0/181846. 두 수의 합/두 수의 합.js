function solution(a, b) {
    var answer = [];
    
    const maxLength = Math.max(a.length, b.length);
    
    a = a.padStart(maxLength, '0');
    b = b.padStart(maxLength, '0');
    
    for(let i=0;i<a.length;i++){
        answer.push(Number(a[i])+Number(b[i]))
    }
    for(let i=answer.length-1;i>0;i--){
        if(answer[i]>=10){
            answer[i-1] += 1
            answer[i] %= 10
        }
    }
    return answer.join('');
}