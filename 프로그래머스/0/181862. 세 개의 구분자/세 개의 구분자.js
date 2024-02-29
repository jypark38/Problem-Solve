function solution(myStr) {
    var answer = [];
    let str = ''
    for(c of myStr){
        if(c=='a'||c=='b'||c=='c'){
            if(str!=''){
                answer.push(str)
                str=''
            }
        } else{
            str+=c
        }
    }
    if(str!='') answer.push(str)
    if(answer.length==0) answer.push('EMPTY')
    return answer;
}