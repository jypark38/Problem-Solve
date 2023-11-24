function solution(s) {
    var answer = [];
    _s = s.split(' ')
    
    for(c of _s){
        let str = ''
        for(let i=0;i<c.length;i++){
            if(i%2 === 0){
                str += c[i].toUpperCase()
            }else{
                str += c[i].toLowerCase()
            }
        }
        answer.push(str)
    }
    
    return answer.join(' ');
}