function solution(s) {
    var answer = 0;
    
    const voca = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    for(let i=0;i<10;i++){
        const n = s.split(voca[i])
        s = n.join(i)
    }
    return s*1;
}