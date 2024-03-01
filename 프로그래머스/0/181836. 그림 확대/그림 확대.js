function solution(picture, k) {
    var answer = [];
    for(c of picture){
        let s = ''
        for(char of c){
            s+=char.repeat(k)
        }
        for(let i=0;i<k;i++){
            answer.push(s)
        }
    }
    return answer;
}